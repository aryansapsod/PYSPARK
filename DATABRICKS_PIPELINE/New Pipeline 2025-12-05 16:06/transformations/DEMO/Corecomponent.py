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
  
  df = dlt.readStream("streaming_table")
  return df

#  Create batch Normal View

@dlt.view(
  name = 'batch_normal_view'
)
def batch_normal_view(): 
  df = spark.read.table("dlt.source.orders")
  return df

# Create Streming View

@dlt.view(
  name = 'streaming_view'
)
def streaming_view(): 
  df = spark.readStream.table("dlt.source.orders")
  return df





