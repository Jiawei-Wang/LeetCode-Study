from models import sensorPacket, ValidationError

class SignalProcessor:
    def __init__(self, window_size=50, max_gap_ms=100):
        self.window_size = window_size
        self.max_gap_ms = max_gap_ms
        self.buffer = []

    def process_raw_data(self, raw_json):
        """
        TODO: 
        1. Validate raw_json using sensorPacket. 
        2. If invalid, return None.
        3. If valid, check the timestamp gap between this packet and the last packet in self.buffer.
        4. If gap > max_gap_ms, clear the buffer.
        5. Append the new packet.
        6. If buffer size > window_size, remove the oldest packet (FIFO).
        7. Return True if the buffer is 'full' (exactly window_size), else False.
        """
        try:
            packet = sensorPacket(**raw_json)   
        except ValidationError:
            return None
        
        if self.buffer:
            last_timestamp = self.buffer[-1].timestamp
            if packet.timestamp - last_timestamp > self.max_gap_ms:
                self.buffer.clear()
        
        self.buffer.append(packet)
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)

        return len(self.buffer) == self.window_size


    def get_window_average_z(self):
        """
        TODO: Return the average accel_z of the current buffer.
        If buffer is empty, return 0.0.
        """
        if not self.buffer:
            return 0.0
        total_z = sum(packet.accel_z for packet in self.buffer)
        return total_z / len(self.buffer)