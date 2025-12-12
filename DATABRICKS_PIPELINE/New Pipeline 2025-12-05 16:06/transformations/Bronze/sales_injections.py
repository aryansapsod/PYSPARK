import dlt

dlt.create_streaming_table(
    name='append_sales'
)

@dlt.append_flow(target='append_sales')
def east_sales():
    df = spark.readStream.table('dlt.bronze')
    return df.filter(df.region == 'east')

@dlt.append_flow(target='append_sales')
def west_sales():
    df = spark.readStream.table('dlt.bronze')
    return df.filter(df.region == 'west')