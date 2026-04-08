WITH movement_markers AS (
    SELECT 
        vehicle_id,
        timestamp,
        is_moving,
        -- Check if the status changed from the previous row
        LAG(is_moving) OVER (PARTITION BY vehicle_id ORDER BY timestamp) as prev_moving
    FROM gps_logs
    WHERE timestamp >= CURRENT_DATE
),
trip_starts AS (
    SELECT 
        vehicle_id
    FROM movement_markers
    -- A trip starts when it is moving NOW, but wasn't moving BEFORE (or it's the first record)
    WHERE is_moving = TRUE 
      AND (prev_moving = FALSE OR prev_moving IS NULL)
)
SELECT 
    vehicle_id, 
    COUNT(*) as total_trips
FROM trip_starts
GROUP BY vehicle_id;