from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 1. Initialize the Spark Session (The entry point to Spark)
spark = SparkSession.builder \
    .appName("Rivian_ETL_Round") \
    .getOrCreate()

# 2. Load the CSV 
# In a real interview, mention: "I'm setting header=True and inferSchema=True, 
# but for production, I'd define a manual schema for better performance."
df = spark.read.csv("telemetry_data.csv", header=True, inferSchema=True)

# 3. Simple Transformation (Data Crunching)
# Example: Filter for high speed and create a 'status' column
processed_df = df.filter(F.col("speed") > 0) \
                 .withColumn("is_overspeed", F.when(F.col("speed") > 80, True).otherwise(False)) \
                 .select("vin", "timestamp", "speed", "is_overspeed")

# 4. Offload to Parquet
# Mention: "I'm partitioning by date to enable efficient data pruning for future queries."
processed_df.write \
    .mode("overwrite") \
    .partitionBy("event_date") \
    .parquet("output_telemetry.parquet")

print("ETL Job Completed Successfully")