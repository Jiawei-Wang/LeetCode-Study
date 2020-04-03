class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # total记录从0到该元素为止所有元素之和
        total = []
        current = 0
        for i in nums:
            current += i
            total.append(current)

        # 步进
        Max = total[k-1]/k
        if len(nums) == k:
            return Max
        else:
            for i in range(k, len(nums)):
                Max = max(Max, (total[i]-total[i-k])/k)

        return Max
