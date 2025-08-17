class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        hashset = set()
        count = 0
        for i in range(length//2):
            average = (nums[i] + nums[length-i-1])/2
            if average not in hashset:
                hashset.add(average)
                count += 1
        return count