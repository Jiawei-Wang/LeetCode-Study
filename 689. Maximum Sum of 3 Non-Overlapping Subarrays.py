# sliding window + dynamic programming
# pick a middle one first, then find biggest left and right ones
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # sum[i] holds the total sum of the first i elements.
        # with this, any window sum can be looked up in O(1): nums[i:i+k] = sum[i+k] - sum[i].
        sum = [0]
        for i in nums:
            sum.append(sum[-1] + i)

        # Left Interval Max Indices:
        # posLeft[i] will store the starting index of the best subarray of length k that ends at or before index i
        # best: biggest sum, or when sum is the same smallest index
        posLeft = [0] * len(nums)
        total = sum[k] - sum[0]
        for i in range(k, len(nums)):
            if sum[i + 1] - sum[i + 1 - k] > total:
                posLeft[i] = i + 1 - k
                total = sum[i + 1] - sum[i + 1 - k]
            else:
                posLeft[i] = posLeft[i - 1]
        # example: [1,2,1,2,6,7,5,1], k = 2
        # posLeft = [0, 0, 0, 0, 3, 4, 4, 4]
        # meaning:
        # first two 0s: [1,2] is the only option
        # 3rd and 4th 0s: [1,2] is the best option (smaller starting index)
        # 3: [2,6] is the best option (biggest sum)
        # 4,4,4: [6,7] is the best option (biggest sum) 

        posRight = [len(nums) - k] * len(nums)
        total = sum[len(nums)] - sum[len(nums) - k]
        for i in range(len(nums) - k - 1, -1, -1):
            # we are going backwards so in order to get same sum smaller starting index
            # we need to use >= total instead of > total
            if sum[i + k] - sum[i] >= total: 
                posRight[i] = i
                total = sum[i + k] - sum[i]
            else:
                posRight[i] = posRight[i + 1]
        
        # dp: test all possible middle interval
        maxsum = 0 # Max total sum found so far (3 subarrays combined)
        ans = [0, 0, 0]
        for i in range(k, len(nums) - 2 * k + 1):
            l = posLeft[i - 1]
            r = posRight[i + k]
            total = (sum[i + k] - sum[i]) + (sum[l + k] - sum[l]) + (sum[r + k] - sum[r])
            if total > maxsum:
                maxsum = total
                ans = [l, i, r]
        return ans