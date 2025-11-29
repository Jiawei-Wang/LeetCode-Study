class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Count number of 1s in nums, this will be the window size
        ones = nums.count(1)

        # Append nums to nums to get rid of circular array part of problem
        nums = nums + nums 

        # Find the maximum number of 1s in window size ones in the new array
        x, onesInWindow = 0, 0
        for i in range(len(nums)):
            if i >= ones and nums[i - ones] == 1: 
                x -= 1
            if nums[i] == 1: 
                x += 1
            onesInWindow = max(x, onesInWindow)

        # Number of swaps = ones - maximum number of 1s in a window of size ones
        return ones - onesInWindow