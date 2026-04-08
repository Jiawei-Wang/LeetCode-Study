-- Phase 1: Data Cleaning
/*
first: data cleaning 
Before joining the data, I need to address two things: Nulls and Outliers. 
I'd filter out any records where GPS coordinates are missing 
or where the speed is physically impossible for a Rivian (e.g., > 130 mph), 
as these would skew our proximity metrics.
*/
WITH cleaned_telemetry AS (
    SELECT *
    FROM telemetry_logs
    WHERE lat IS NOT NULL 
      AND lng IS NOT NULL
      AND speed_mph BETWEEN 0 AND 130
)

-- Phase 2: The Spatial Filter (SQL)
-- Since we have billions of rows, a "Cross Join" (comparing every vehicle ping to every service center) 
-- is $O(N * M) and will crash the cluster.
SELECT DISTINCT t.vehicle_id
FROM cleaned_telemetry t
JOIN service_centers s 
  ON t.lat BETWEEN s.center_lat - 0.8 AND s.center_lat + 0.8  -- Rough 50-mile box
  AND t.lng BETWEEN s.center_lng - 0.8 AND s.center_lng + 0.8
WHERE ST_Distance(ST_Point(t.lng, t.lat), ST_Point(s.center_lng, s.center_lat)) <= 80467 -- 50 miles in meters



