# import dlt
# from pyspark.sql.functions import *

# # Creating End To End Pipeline

# #  Staging Area

# @dlt.table(
#     name = "staging_orders"
# )
# def staging_orders():
#     # return(
#     #     spark.readStream.format('cloudFiles') 

#     # )
#     df = spark.readStream.table('dlt.source.orders')
#     # df = df.withColumn
#     return df



# #  Creating Transform Area


# @dlt.table(
#     name="transform_orders"
# )

# def transform_orders():
#     df =spark.readStream.table('staging_orders')
#     df = df.withColumn("orderstatus",lower(col("order_status")))

    
#     return df


# #  Creating Agrigating Area

# @dlt.table(
#     name="aggregating_orders"
# )
# def aggregating_orders():
#     df = spark.readStream.table('transform_orders')
#     df = df.groupBy("orderstatus").count()
#     return df


