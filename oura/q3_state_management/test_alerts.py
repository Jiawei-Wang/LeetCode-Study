import time
import unittest

from alert_manager import AlertManager
from storage import db

class TestAlerts(unittest.TestCase):
    def test_alerts(self):
        # Clear the mock database before testing
        db._data.clear()

        alert_manager = AlertManager(quiet_period_seconds=2)

        user_id = "user123"
        incident_type = "fall"

        # First alert should be dispatched
        self.assertTrue(alert_manager.should_dispatch(user_id, incident_type))

        # Immediately after, it should not be dispatched
        self.assertFalse(alert_manager.should_dispatch(user_id, incident_type))

        # Check remaining cooldown (should be close to 2 seconds)
        remaining_cooldown = alert_manager.get_remaining_cooldown(user_id, incident_type)
        self.assertTrue(1.5 < remaining_cooldown <= 2)

        # Wait for the quiet period to expire
        time.sleep(2)

        # Now it should be dispatched again
        self.assertTrue(alert_manager.should_dispatch(user_id, incident_type))

if __name__ == "__main__":
    unittest.main()