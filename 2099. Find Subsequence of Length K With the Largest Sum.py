class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # find subsequence not subarray
        # 1. get the k biggest values in nums
        values = []
        for idx, num in enumerate(nums):
            values.append((num, idx))
        values.sort(reverse=True)
        # 2. pick these k biggest values and store their indexes
        indexes = []
        for i in range(k):
            indexes.append(values[i][1])
        indexes.sort()
        # 3. use the indexes to reassemble the subsequence
        answer = []
        for index in indexes:
            answer.append(nums[index])
        return answer