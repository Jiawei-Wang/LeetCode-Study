class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        current_gap = 10000 # -1000 <= nums[i] <= 1000
        current_streak = 0

        answer = 0

        for i in range(len(nums)-1):
            first = nums[i]
            second = nums[i+1]
            gap = second - first
        
            if current_gap == 10000 or current_gap != gap:
                current_gap = gap
                current_streak = 1
            else:
                current_streak += 1
                if current_streak >= 2:
                    answer += current_streak - 1
                    """
                    for 1, 3, 5:        streak = 2, subarray = 1
                    for 1, 3, 5, 7:     streak = 3, subarray = 3
                    for 1, 3, 5, 7, 9:  streak = 4, subarray = 6
                    """
        
        return answer
