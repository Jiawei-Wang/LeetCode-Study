import time

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        """
        :param max_requests: Maximum allowed requests per window
        :param window_seconds: The duration of the sliding window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # TODO: Choose a data structure to track timestamps per user
        self.calls = {}

    def is_allowed(self, user_id: str) -> bool:
        """
        TODO:
        1. Get the current time (Unix timestamp).
        2. Retrieve the list of timestamps for this user_id.
        3. Filter out/remove any timestamps that are older than (current_time - window_seconds).
        4. If the number of remaining timestamps is < max_requests:
           - Add the current timestamp to the list.
           - Return True.
        5. Otherwise, return False.
        """
        current_time = time.time()
        if user_id not in self.calls:
            self.calls[user_id] = []
        
        # Filter out old timestamps
        self.calls[user_id] = [timestamp for timestamp in self.calls[user_id] if timestamp > current_time - self.window_seconds]
        
        if len(self.calls[user_id]) < self.max_requests:
            self.calls[user_id].append(current_time)
            return True
        else:
            return False
        

"""
Followups:
1. performance bottleneck: 
    if a user calls very frequently, the array needs to be modified a lot, which causes issues.
2. logic to purge old users with no recent activity: 
    implement Time To Live by storing last_updated timestamp for each user and purge periodically.
3. improve the bottleneck:
    circular array
4. distributed backend:
    Redis
"""