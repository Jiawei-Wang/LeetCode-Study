The Efficient Metric Aggregator

Problem: Process a high-volume stream of data and provide real-time statistics without storing every single data point (which would eventually crash your server's memory).

The Scenario: Your service receives "Heart Rate" events. You need to provide the Moving Average of the last $N$ samples and the Maximum value seen so far.


The Task

Implement a class MetricTracker that supports two main operations:

add_sample(value: int): Adds a new heart rate reading.

get_stats(): Returns the current average of the "window" and the all-time maximum.