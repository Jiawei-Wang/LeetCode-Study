class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hour_curr = int(current[0:2])
        minute_curr = int(current[3:5])

        hour_target = int(correct[0:2])
        minute_target = int(correct[3:5])

        if hour_curr > hour_target or (hour_curr == hour_target and minute_curr > minute_target):
            hour_target += 24

        total_minute = 60 * (hour_target - hour_curr) + minute_target - minute_curr

        ops = total_minute // 60
        total_minute %= 60
        ops += total_minute // 15
        total_minute %= 15
        ops += total_minute // 5
        total_minute %= 5
        ops += total_minute
    
        return ops
