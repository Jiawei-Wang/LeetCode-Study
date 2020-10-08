class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 30 * hour + 0.5 * minutes
        m = 6 * minutes
        if h > m:
            if h - m <= 180:
                return h-m
            else:
                return m-h+360
        else:
            if m-h <= 180:
                return m-h
            else:
                return h+360-m
