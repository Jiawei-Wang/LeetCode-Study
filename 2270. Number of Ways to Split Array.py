class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [] # prefix_sum[i] = k: nums[0:i+1] has sum k
        suffix_sum = [] # suffix_sum[i] = k: nums[i+1:] has sum k

        remain = sum(nums)
        total = 0

        for index in range(len(nums)):
            curr = nums[index]
            total += curr
            prefix_sum.append(total)
            remain -= curr
            suffix_sum.append(remain)
        
        counter = 0
        for index in range(len(nums)-1):
            if prefix_sum[index] >= suffix_sum[index]:
                counter += 1
        return counter

        