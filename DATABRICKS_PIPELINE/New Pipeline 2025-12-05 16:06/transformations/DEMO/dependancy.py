import dlt

# Creating End To End Pipeline

#  Staging Area

@dlt.table(
    name = "staging_orders"
)
def staging_orders():
    # return(
    #     spark.readStream.format('cloudFiles') 

    # )
    df = spark.readStream.table('dlt.source.orders')
    return df



#  Creating Transform Area


@dlt.table(
    name="transform_orders"
)

def transform_orders():
    df =spark.readStream.table('staging_orders')
    
    return df

    