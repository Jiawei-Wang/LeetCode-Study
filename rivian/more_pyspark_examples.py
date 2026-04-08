# 1) The "Vehicle Sessionization" (Gaps and Islands)
# This is a classic autonomy problem: taking a stream of "active" pings and grouping them into distinct "trips." 
# A trip ends if we don't hear from the car for more than 10 minutes.

from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Assuming df has: vin, ts (timestamp)
window_spec = Window.partitionBy("vin").orderBy("ts")

# 1. Calculate time difference between current and previous ping
df_with_gap = df.withColumn("prev_ts", F.lag("ts").over(window_spec)) \
                .withColumn("diff_minutes", (F.col("ts").cast("long") - F.col("prev_ts").cast("long")) / 60)

# 2. Identify a "New Trip" start (1 if it's a new trip, 0 if it's a continuation)
df_is_new_trip = df_with_gap.withColumn(
    "is_new_trip", 
    F.when(F.col("diff_minutes") > 10, 1).otherwise(0)
)

# 3. Use a Running Sum to create a unique Trip ID
df_trips = df_is_new_trip.withColumn(
    "trip_id", 
    F.sum("is_new_trip").over(window_spec.rowsBetween(Window.unboundedPreceding, 0))
)


# 2) The "Broadcast Join" for Metadata
# Imagine you have billions of sensor pings and a small table of "Vehicle Metadata" (e.g., model type, battery capacity).
from pyspark.sql.functions import broadcast

# df_telemetry = billions of rows
# df_vehicle_info = 100k rows (small enough to fit in memory)

# We use broadcast() to send the small table to every worker node.
# This avoids a "Shuffle," which is the most expensive operation in Spark.
df_enriched = df_telemetry.join(
    broadcast(df_vehicle_info), 
    on="vin", 
    how="left"
)


# 3) Writing Optimized Data (The "Refinery" Step)
# After you've crunched the data, how you save it determines how fast the next team can query it.
(df_enriched
 .write
 .mode("overwrite")
 .partitionBy("event_date", "model_type") # Crucial for data pruning
 .option("compression", "snappy")         # Standard balance of speed/ratio
 .parquet("s3://rivian-data-lake/gold/vehicle_events/"))

 

# Polyglot Programming
# 1. Load your data
df = spark.read.parquet("s3://rivian-data/raw/telemetry")

# 2. Register it as a temporary view
df.createOrReplaceTempView("telemetry_table")

# 3. Write standard SQL
query = """
SELECT 
    vin, 
    ts, 
    velocity,
    velocity - LAG(velocity) OVER (PARTITION BY vin ORDER BY ts) as acceleration
FROM telemetry_table
WHERE velocity IS NOT NULL
"""

# 4. Execute and get a DataFrame back
df_accelerated = spark.sql(query)

# 5. Continue using Python/PySpark on the result
df_final = df_accelerated.filter("acceleration > 5")