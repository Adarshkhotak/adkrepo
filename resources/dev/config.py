import os

key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"

#AWS Access And Secret key
aws_access_key = "xV8gLLZ4OPnngCZ1wOVWV9KZ3uWKJ4zd1UKCK2tR3Zc="
aws_secret_key = "mBFCiO/PWA39UXJkB2ytr3cszOlV6vr/bnA3n+H8PorUd4GxMvJ9p8NmhaMuiqRI"
bucket_name = "youtube-project-testing-sam"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


#Database credential
# MySQL database connection properties
database_name = "project_sam"
url = "jdbc:mysql://localhost:3306/project_sam"
properties = {
    "user": "root",
    "password": "mysql",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "D:\\Project_Data\\filefrom_s3"
customer_data_mart_local_file = "D:\\Project_Data\\cust_datamart"
sales_team_data_mart_local_file = "D:\\Project_Data\\sales_team_datamart"
sales_team_data_mart_partitioned_local_file = "D:\\Project_Data\\sales_partitiondata"
error_folder_path_local = "D:\\Project_Data\\error_files"
