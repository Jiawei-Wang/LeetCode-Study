import time
from storage import db

class AlertManager:
    def __init__(self, quiet_period_seconds=300):
        self.quiet_period = quiet_period_seconds

    def should_dispatch(self, user_id, incident_type):
        """
        TODO:
        1. Create a unique key using user_id and incident_type.
        2. Check the 'storage' to see the last time this specific alert was sent.
        3. Logic:
           - If the alert has NEVER been sent, or was sent MORE than 
             quiet_period_seconds ago, return True.
           - Otherwise, return False.
        4. If returning True, update the storage with the current timestamp.
        """
        key = f"{user_id}:{incident_type}"
        last_sent_time = db.get(key)

        current_time = time.time()
        if last_sent_time is None or (current_time - last_sent_time) > self.quiet_period:
            db.set(key, current_time)
            return True
        else:
            return False


    def get_remaining_cooldown(self, user_id, incident_type):
        """
        TODO: Return how many seconds are left before this alert can be sent again.
        Return 0 if it can be sent now.
        """
        key = f"{user_id}:{incident_type}"
        last_sent_time = db.get(key)

        if last_sent_time is None:
            return 0
        
        elapsed_time = time.time() - last_sent_time
        remaining_cooldown = self.quiet_period - elapsed_time
        return max(0, remaining_cooldown)
        