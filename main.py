import datetime
import os.path
import shutil
import mysql.connector

from pyspark.sql.functions import concat_ws, lit
from pyspark.sql.types import StructField, StringType, IntegerType, StructType, DateType, FloatType

from resources.dev import config
from src.main.download.aws_file_download import S3FileDownloader
from src.main.move.move_files import move_s3_to_s3
from src.main.read.database_read import DatabaseReader
from src.main.utility.encrypt_decrypt import *
from src.main.utility.s3_client_object import *
from src.main.utility.logging_config import *
from src.main.utility.my_sql_session import *
from resources.dev import config
from src.main.read.aws_read import *
from src.main.utility.spark_session import spark_session
####################Get S3 client ##################


aws_access_key = config.aws_access_key
#aws_access_key = "BoDD3/AeLULfó/nzioHdA5X/qL6p1MZk0EZSW7+YowE="
aws_secret_key= config.aws_secret_key
s3_client_provider = S3ClientProvider(decrypt(aws_access_key), decrypt(aws_secret_key))
s3_client= s3_client_provider.get_client()
#Now you can use s3_client for your $3 operations
response = s3_client.list_buckets()
print(response)
logger.info("List of Buckets: %s", response ['Buckets'])



#check if local directory has already file
#iffile is there then check if the same file is present in staging area
#with status as A. if so then dont delete and try to re run
#else give an error and not process the next file
#csv_files = [file for file in os.listdir(config.local_directory) if file.endswith(".csv")]
csv_files = [file for file in os.listdir(config.local_directory) if file.lower().endswith((".csv", ".xlsx"))]

connection = get_mysql_connection()
cursor = connection.cursor()

total_csv_files=[]
if csv_files: #not_empty==true
    for file in csv_files:
        total_csv_files.append(file)

    statement = f"""
    select distinct file_name from project_sam.product_staging_table 
    
    where file_name in ({str(total_csv_files)[1:-1]}) and status='A' """

    logger.info(f"dynamically statement created: {statement}")
    cursor.execute(statement)
    data = cursor.fetchall()
    if data:
        logger.info("your last run was failed please check")
    else:
        logger.info("no record match")

else:
    logger.info("last run was successful!!!")


try:
    s3_reader = S3Reader()
    # Bucket name should come from table
    folder_path = config.s3_source_directory
    s3_absolute_file_path = s3_reader.list_files(s3_client,
                                                 config.bucket_name,
                                                 folder_path = folder_path)
    logger.info("Absolute path on s3 bucket for csv file %s ",s3_absolute_file_path)
    if not s3_absolute_file_path:
        logger.info(f"No files available at {folder_path}")
        raise Exception("No Data avaliable to process")

except Exception as e:
    logger.error("Exited with error:- %s ",e)
    raise e

# ['s3://youtube-project-testing-sam/sales_data/Boat.JoinTable.csv', 's3://youtube-project-testing-sam/sales_data/sales_data.csv']


from logging import *

bucket_name = config.bucket_name
local_directory = config.local_directory

prefix =  f"s3://{bucket_name}/"
file_path = [url[len(prefix):] for url in s3_absolute_file_path]
#logging.info(msg:"File path available on s3 under %s bucket and folder name is %s",*args: bucket_name , file_path)
logging.info(f"File path available on s3 under {bucket_name} bucket and folder name is {file_path}")
try:
    downloader = S3FileDownloader(s3_client , bucket_name,local_directory)
    downloader.download_files(file_path)
except Exception as e:
    logger.error("File download error: %s",e)
    sys.exit()

#Get a list of all files in the local directory
all_files= os.listdir(local_directory)
logger.info(f"List of files present at my local directory after dawnload {all_files}")

#Filter files with ".csv" in their names and create absolute paths
if all_files:
    csv_files=[]
    error_files=[]
    for files in all_files:
        if file.endswith(".csv"):
            csv_files.append(os.path.abspath(os.path.join(local_directory, files)))
        else:
            error_files.append(os.path.abspath(os.path.join(local_directory,files)))
    if not csv_files:
        logger.error("No CSV data avaliable to process the request")
        raise Exception("No csv data avaliable to process the request")

######### make csv lines aonvert into a list of comma separated ##########
#csv_files = str(csv_files)[1:-1]
logger.info("*****************Listing the file*******************")
logger.info("List of csv files that needs to be processed %s", csv_files)

logger.info("******************Creating Spark session ***************")
spark = spark_session()

logger.info("**********Spark session created ***************")

#check the required column in the schema of csv files
#if not required columns keep it in a list or error files
#else union all the data into one dataframe

logger.info("**********Checking schema for data loaded in s3 ****")
correct_files =[]
for data in csv_files:
    data_schema = spark.read.format("csv")\
        .option("header","true")\
        .load(data).columns

    logger.info(f"Schema for the {data} is {data_schema} ")
    logger.info(f"Mandatory columns schema is {config.mandatory_columns}")
    missing_columns= set(config.mandatory_columns)- set(data_schema)
    logger.info(f"missing columns are {missing_columns}")

    if missing_columns:
        error_files.append(data)
    else:
        logger.info(f"No missing columns for {data}")
        correct_files.append(data)


logger.info(f"********* List of correct files ********{correct_files}")
logger.info(f"**********List of error files ********{error_files}")
logger.info("********Moving error data to error directory if any **********")

#Move the data to error directory on local
error_folder_local_path = config.error_folder_path_local
if error_files:
    for file_path in error_files:
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(error_folder_local_path,file_name)

            shutil.move(file_path,destination_path)
            logger.info(f"Moved '{file_name}' from s3 file path to '{destination_path}'")

            source_prefix = config.s3_source_directory
            destination_prefix = config.s3_error_directory

            message = move_s3_to_s3(s3_client,config.bucket_name,source_prefix,destination_prefix,file_name)
            logger.info(f"{message}")
        else:
            logger.error(f"'{file_path}' does not exist")


else:
    logger.info("********** There is no error file available at our dtaset ***********")




#Additionally columns needs to be taken care of
# Determine extra columns

#Before running the process
#stage table needs to be updated with status as Active (A) or inactive (I)

logger.info((f"************* Updating the product_staging_table that we have started the process**********"))
insert_statements = []
db_name = config.database_name
current_date = datetime.datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
if correct_files:
    for file in correct_files:
        filename = os.path.basename(file)
        statements=f" INSERT INTO {db_name}.{config.product_staging_table}"\
                    f"(file_name , file_location , created_date,status)"\
                    f"VALUES ('{filename}','{filename}','{formatted_date}','A')"

        insert_statements.append(statements)
    logger.info(f"Insert statement created for staging table---{insert_statements}")
    logger.info("************Connecting with MY SQL server **********")
    connection = get_mysql_connection()
    cursor = connection.cursor()
    logger.info("******* MY SQL server connected successfully *******")
    for statement in insert_statements:
        cursor.execute(statement)
        connection.commit()
    cursor.close()
    connection.close()

else:
    logger.error("****There is no files to process ****")
    raise Exception("*******No data avalable with correct files **********")


logger.info("************* Staging table updated succesfully **************")

logger.info("****************** Fixing extra coming from source *******************")

schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("store_id", IntegerType(), True),
    StructField("product_name", StringType(), True),
    StructField("sales_date", DateType(), True),
    StructField("sales_person_id", IntegerType(), True),
    StructField("price", FloatType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("total_cost", FloatType(), True),
    StructField("additional_column", StringType(), True)
])


#connecting with DatabaseReader
database_client = DatabaseReader(config.url,config.properties)
logger.info(("************ creating empty datframe **************"))
final_df_to_process = database_client.create_dataframe(spark,"empty_df_create_table")
final_df_to_process.show()

#final_df_to_process = spark.createDataFrame([], schema = schema)
#create a new column with concatenated values of extra columns
for data in correct_files:
    data_df = spark.read.format(("csv"))\
        .option("header","true")\
        .option("InferSchema","true")\
        .load(data)
    data_schema = data_df.columns
    extra_columns = list(set(data_schema) - set(config.mandatory_columns))
    logger.info(f"Extra columns at source is {extra_columns}")
    if extra_columns:
        data_df = data_df.withColumn("additional_column",concat_ws(",",*extra_columns))\
                .select("customer_id","store_id","product_name","sales_date","sales_person_id",
                        "price","quantity","total_cost","additional_column")

        logger.info(f"Processed {data} and added 'additional_column'")
    else:
        data_df= data_df.withColumn("additional_column",lit(None))\
            .select("customer_id","store_id","product_name","sales_date","sales_person_id",)


    final_df_to_process = final_df_to_process.union(data_df)
# final_df_to_process =data_df
logger.info("**** Final dataframe from source which will be going processing*****")
final_df_to_process.show()