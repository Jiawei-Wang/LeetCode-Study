class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(capacity):
            total_days = 1
            total_weight = 0
            for package in weights:
                total_weight += package
                if total_weight > capacity:
                    total_days += 1
                    total_weight = package
            return total_days <= days

        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high-low)//2
            if is_valid(mid):
                high = mid
            else:
                low = mid + 1

        return low