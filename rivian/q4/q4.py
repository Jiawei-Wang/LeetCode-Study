"""
plain python for solving aggressive braking problem (drop > 20 mph in 2 seconds)

algorithm: sliding indow
one pointer represents the current ping, the other represents the earliest ping within the 2 second window
"""

def find_aggressive_braking(telemetry_data):
    """
    telemetry_data: List of dicts sorted by timestamp
    [{'ts': 1600000000, 'vel': 60}, {'ts': 1600000001, 'vel': 55}, ...]
    """
    results = []
    left = 0  # Our "back-in-time" pointer
    
    for right in range(len(telemetry_data)):
        current_ping = telemetry_data[right]
        
        # 1. Shrink the window from the left 
        # Ensure the 'left' ping is within 2 seconds of the 'right' ping
        while current_ping['ts'] - telemetry_data[left]['ts'] > 2:
            left += 1
        
        # 2. Check all pings within that 2-second window
        # (Usually, you compare the current speed to the MAX speed in the window)
        start_vel = telemetry_data[left]['vel']
        current_vel = current_ping['vel']
        
        if (start_vel - current_vel) > 20:
            results.append({
                'vin': current_ping['vin'],
                'ts': current_ping['ts'],
                'drop': start_vel - current_vel
            })
            # Optional: Move left to right to avoid duplicate flags for the same event
            left = right 
            
    return results


"""
pyspark
"""

# 1. define the window
# We need to look at data partitioned by vin and ordered by ts.
from pyspark.sql import Window
import pyspark.sql.functions as F
window_spec = Window.partitionBy("vin").orderBy("ts")

# 2. get previous speed
# To find a drop over 2 seconds, we need to compare the current row to a row from 2 seconds ago.
# Grab the velocity from 20 rows ago (assuming 10Hz data)
df_with_lag = df_telemetry.withColumn(
    "prev_velocity", 
    F.lag("velocity", 20).over(window_spec)
)

# 3. filter the events
# Calculate the drop and filter
aggressive_braking_events = df_with_lag.withColumn(
    "speed_drop", F.col("prev_velocity") - F.col("velocity")
).filter("speed_drop > 20")
aggressive_braking_events.select("vin", "ts").show()


# read and write
spark.read.parquet("s3://bucket/raw_data/")
df.write.partitionBy("date").parquet("s3://bucket/gold_data/")