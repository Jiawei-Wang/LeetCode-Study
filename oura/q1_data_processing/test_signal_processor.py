import unittest
from signal_processor import SignalProcessor

class TestSignalProcessor(unittest.TestCase):
    def test_flow(self):
        proc = SignalProcessor(window_size=3, max_gap_ms=100)
        
        # Test 1: Validation & Filling
        proc.process_raw_data({"timestamp": 1000, "accel_x": 1, "accel_y": 1, "accel_z": 5.0})
        self.assertEqual(len(proc.buffer), 1)
        
        # Test 2: Gap Detection
        proc.process_raw_data({"timestamp": 2000, "accel_x": 1, "accel_y": 1, "accel_z": 5.0})
        self.assertEqual(len(proc.buffer), 1, "Buffer should have cleared due to 1000ms gap")

        # Test 3: Buffer Management
        proc.process_raw_data({"timestamp": 2100, "accel_x": 1, "accel_y": 1, "accel_z": 5.0})
        proc.process_raw_data({"timestamp": 2200, "accel_x": 1, "accel_y": 1, "accel_z": 6.0})
        self.assertEqual(len(proc.buffer), 3, "Buffer should have 3 packets")   

        # Test 4: Buffer Overflow
        proc.process_raw_data({"timestamp": 2300, "accel_x": 1, "accel_y": 1, "accel_z": 7.0})
        self.assertEqual(len(proc.buffer), 3, "Buffer should still have 3 packets after overflow")
        self.assertEqual(proc.buffer[0].timestamp, 2100, "Oldest packet should have been removed")

        # Test 5: Window Average Calculation
        avg_z = proc.get_window_average_z()
        self.assertEqual(avg_z, 6.0, "Average accel_z should be 6.0")
        proc.buffer.clear()
        avg_z_empty = proc.get_window_average_z()
        self.assertEqual(avg_z_empty, 0.0, "Average accel_z should be 0.0 for empty buffer")

if __name__ == "__main__":
    unittest.main()