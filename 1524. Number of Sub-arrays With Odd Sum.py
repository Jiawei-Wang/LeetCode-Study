class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [arr[0] % 2]
        """
        dp[i] = k: there are k subarrays with odd sum ending at index i
        from 0-0 to 0-i there are in total i+1 subarrays
        so there are i+1-k subarrays that have even sum

        dp[0] = 1: 0-th element is odd therefore 1 subarray with odd sum ending at index 0
        dp[0] = 0: 0-th element is even therefore 0 subarray with odd sum ending at index 0
        """

        for i in range(1, len(arr)):
            is_odd = arr[i] % 2
            if is_odd: # if new number is odd
                # for i-1 th element, we have dp[i-1] odd sum subarrays
                # so we have (i-1) + 1 - dp[i-1] even sum subarrays
                # all of them can form odd sum subarray with new element
                # plus 1 that is the new element as standalone subarray
                dp.append(i - dp[i-1] + 1)
            else: # if new number is even
                dp.append(dp[i-1]) # we just take dp[i-1]
        
        return sum(dp) % (10 ** 9 + 7)


