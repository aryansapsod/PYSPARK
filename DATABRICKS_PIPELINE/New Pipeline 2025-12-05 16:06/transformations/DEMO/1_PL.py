# Creating straming table

import dlt

@dlt.table(
  name = "streaming_table",

)
def first_stream_table():
   
   df = spark.readStream.table("dlt.source.orders")
   return df
a