# Creating straming table

import dlt

@dlt.table(
  name = "streaming_table",

)
def first_stream_table():
   
   df = spark.readStream.table("dlt.source.orders")
   return df
 
@dlt.table(
  name = 'first_mat_view'
)

def first_mat_view():
  
  df = dlt.read("streaming_table")







