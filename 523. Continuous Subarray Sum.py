# 从nums中找到一个长度至少为2的subarray，其总和为k的倍数（0也是倍数）

# 暴力解
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+2, len(nums)+1):
                subarray = nums[i:j]
                if not sum(subarray) % k:
                    return True
        return False
        

# 暴力解优化
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                curr += nums[j]
                if not curr % k:
                    return True
        return False


# Idea: if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. 
# So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i. 
# Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.
# Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False
        