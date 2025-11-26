class Solution:
    def numberOfSubarrays(self, nums, k):
        left = 0
        odd_count = 0
        ans = 0
        prefix = 0  # number of evens at window start

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
                prefix = 0  # reset when a new odd enters

            # If we have too many odds, shrink until we have exactly k
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            # Once we have exactly k odds, count valid left positions
            while odd_count == k and nums[left] % 2 == 0:
                prefix += 1
                left += 1

            # If window has exactly k odds, add prefix + 1 valid subarrays
            if odd_count == k:
                ans += prefix + 1

        return ans
