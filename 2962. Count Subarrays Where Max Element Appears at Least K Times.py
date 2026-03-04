class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)  # O(n)
        ans = 0
        left = 0
        count = 0
        
        for right in range(len(nums)):
            # If we find the max element, increment our counter
            if nums[right] == max_val:
                count += 1
            
            # While the window is valid (has at least k max_vals),
            # shrink it from the left to find the 'boundary'
            while count == k:
                if nums[left] == max_val:
                    count -= 1
                left += 1
            
            # All subarrays starting from index 0 to left-1 
            # and ending at 'right' are valid.
            ans += left
            
        return ans