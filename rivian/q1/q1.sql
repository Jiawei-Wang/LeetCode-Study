SELECT vehicle_id, 
       AVG(duration) as avg_session
FROM (
    SELECT vehicle_id, 
           timestamp - LAG(timestamp) OVER (PARTITION BY vehicle_id ORDER BY timestamp) as duration
    FROM sensor_events
    WHERE event_name = 'HighwayAssist_Deactivated' -- Simplified logic
)
GROUP BY vehicle_id;

-- instead of self join 
-- do a window function to calculate the duration between events for each vehicle
-- lag(timestamp): look back at a previous row
-- partition by vehicle_id: group rows by vehicle_id before doing the calculation
-- order by timestamp: ensure the events are in chronological order for each vehicle