from collections import deque

class MetricTracker:
    def __init__(self, window_size: int):
        """
        :param window_size: The number of recent samples to include in the average.
        """
        self.window_size = window_size
        # TODO: Initialize your data structures
        # Think about how to calculate the average in O(1) time
        self.window = deque()
        self.all_time_max = float('-inf')

    def add_sample(self, value: int):
        """
        TODO:
        1. Add the new value to the sliding window.
        2. If the window exceeds window_size, remove the oldest.
        3. Update the 'all-time' maximum if this value is higher.
        """
        self.window.append(value)
        if len(self.window) > self.window_size:
            self.window.popleft()
        
        if value > self.all_time_max:
            self.all_time_max = value

    def get_stats(self) -> dict:
        """
        TODO: Return a dictionary with:
        - "moving_avg": float
        - "all_time_max": int
        """
        moving_avg = sum(self.window) / len(self.window) if self.window else 0.0
        return {
            "moving_avg": moving_avg,
            "all_time_max": self.all_time_max
        }