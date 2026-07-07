"""
to make the difference = max - min smaller, 
moves should be used to eliminate extreme values:
change a very big outlier to match a middle number
change a very small outlier to match a middle number
four possible scenarios:
1. kill 3 largest numbers
2. kill 2 largest and 1 smallest
3. kill 1 largest an 2 smallest
4. kill 3 smallest numbers
(if array has <= 4 numbers, diff is always 0 after 3 moves)
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        # If there are 4 or fewer elements, we can change 3 of them 
        # to match the 4th one, making the difference 0.
        if n <= 4:
            return 0
        
        # Sort the array to easily identify the smallest and largest elements
        nums.sort()
        
        # We evaluate the 4 possible scenarios after eliminating 3 extreme elements:
        # Scenario 1: Eliminate 3 largest. New min is nums[0], new max is nums[n-4]
        # Scenario 2: Eliminate 1 smallest, 2 largest. New min is nums[1], new max is nums[n-3]
        # Scenario 3: Eliminate 2 smallest, 1 largest. New min is nums[2], new max is nums[n-2]
        # Scenario 4: Eliminate 3 smallest. New min is nums[3], new max is nums[n-1]
        
        res = min(
            nums[n - 4] - nums[0],  # Case 1
            nums[n - 3] - nums[1],  # Case 2
            nums[n - 2] - nums[2],  # Case 3
            nums[n - 1] - nums[3]   # Case 4
        )
        
        return res