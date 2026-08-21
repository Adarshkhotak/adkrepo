# +---------+-------------------+-------------+
 
# | user_id |     timestamp     | device_type |

# +---------+-------------------+-------------+
 
# |   U1    | 2026-08-20 10:00:00|    Mobile   |

# |   U1    | 2026-08-20 10:15:00|    Mobile   |

# |   U1    | 2026-08-20 10:50:00|    Mobile   | 

# |   U1    | 2026-08-20 10:55:00|    Desktop  | 

# |   U2    | 2026-08-20 11:00:00|    Mobile   |

# +---------+-------------------+-------------+

 
# +---------+-------------------+-------------+------------+
 
# | user_id |     timestamp     | device_type | session_id |

# +---------+-------------------+-------------+------------+
 
# |   U1    | 2026-08-20 10:00:00|    Mobile   |    U1_1    |

# |   U1    | 2026-08-20 10:15:00|    Mobile   |    U1_1    |

# |   U1    | 2026-08-20 10:50:00|    Mobile   |    U1_2    |

# |   U1    | 2026-08-20 10:55:00|    Desktop  |    U1_3    |

# |   U2    | 2026-08-20 11:00:00|    Mobile   |    U2_1    |

# +---------+-------------------+-------------+------------+

df = spark.createDataFrame(data, columns) \
          .withColumn("timestamp", F.to_timestamp("timestamp"))
 
# 2. Window specification ordered by timestamp per user
window_spec = Window.partitionBy("user_id").orderBy("timestamp")
 
# 3. Get previous row's timestamp and device_type
df_lag = df.withColumn("prev_ts", F.lag("timestamp").over(window_spec)) \
           .withColumn("prev_device", F.lag("device_type").over(window_spec))
 
# 4. Identify session breaks (>30 min gap OR device change)
df_flag = df_lag.withColumn(
    "time_diff_minutes",
    (F.col("timestamp").cast("long") - F.col("prev_ts").cast("long")) / 60
).withColumn(
    "new_session_flag",
    F.when(
        (F.col("prev_ts").isNull()) |
        (F.col("time_diff_minutes") > 30) |
        (F.col("device_type") != F.col("prev_device")),
        1
    ).otherwise(0)
)
 
# 5. Calculate cumulative sum to form session index per user
window_sum = Window.partitionBy("user_id").orderBy("timestamp").rowsBetween(Window.unboundedPreceding, Window.currentRow)
 
df_session = df_flag.withColumn("session_num", F.sum("new_session_flag").over(window_sum)) \
                    .withColumn("session_id", F.concat(F.col("user_id"), F.lit("_"), F.col("session_num")))
 
# 6. Final Selection
output_df = df_session.select("user_id", "timestamp", "device_type", "session_id")
output_df.show(truncate=False)

#############################
+---------+------------+----------+
 
| item_id |    date    | adjusted |

+---------+------------+----------+
 
|  ITEM_A | 2026-08-17 |    10    |

|  ITEM_A | 2026-08-18 |    -2    |

|  ITEM_A | 2026-08-20 |     5    | 

+---------+------------+----------+


 
+---------+------------+---------------+
 
| item_id |    date    | current_stock |

+---------+------------+---------------+
 
|  ITEM_A | 2026-08-17 |      10       |

|  ITEM_A | 2026-08-18 |       8       |

|  ITEM_A | 2026-08-19 |       8       |

|  ITEM_A | 2026-08-20 |      13       |

+---------+------------+---------------+
 df = spark.createDataFrame(data, columns).withColumn("date", F.to_date("date"))
 
# 2. Find min and max date per item to generate a complete date range
date_range_df = df.groupBy("item_id").agg(
    F.min("date").alias("min_date"),
    F.max("date").alias("max_date")
).select(
    "item_id",
    F.explode(F.sequence("min_date", "max_date", F.expr("INTERVAL 1 DAY"))).alias("date")
)
 
# 3. Join filled date range with original data
filled_df = date_range_df.join(df, on=["item_id", "date"], how="left")
 
# 4. Define Window for Running Total
windowSpec = Window.partitionBy("item_id").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
 
# 5. Calculate cumulative stock by treating null adjustments as 0
output_df = filled_df.withColumn(
    "current_stock",
    F.sum(F.coalesce(F.col("adjusted"), F.lit(0))).over(windowSpec)
).select("item_id", "date", "current_stock")
 
output_df.show()

################
#Find non duplicate from table using Window functions
WITH RecordCounts AS (
    SELECT
        *,
        COUNT(*) OVER (
            PARTITION BY col1, col2, col3 -- List all columns that define a record
        ) AS total_occurrences
    FROM my_table
)
SELECT
    col1,
    col2,
    col3
FROM RecordCounts
WHERE total_occurrences = 1;
