"""
Phase 3: Handling the "Big Data" Crunch (Python/Spark)
In Python, if this data doesn't fit in a single machine's memory, I’d use PySpark. 
To avoid a 'Shuffle', I would Broadcast the service_centers table. 
Since it’s small, sending a copy to every worker node avoids moving the billions of telemetry rows across the network.
"""
from pyspark.sql.functions import broadcast

# Clean outliers
df_clean = df_telemetry.filter("speed_mph < 130 AND lat IS NOT NULL")

# Use a Broadcast Join for efficiency
# This sends the small centers table to every node
joined_df = df_clean.join(broadcast(df_centers), "region_id") 

# Vectorized distance calculation using a UDF or built-in math

"""
Phase 4: Pro-level Optimization with Data Partitioning.
Finally, since telemetry is time-series, 
I’d ensure the raw data is partitioned by date and hex_id (like Uber’s H3 index). 
This allows us to only scan the specific geographic 'tiles' and timeframes we care about, 
rather than the entire global fleet history.
"""