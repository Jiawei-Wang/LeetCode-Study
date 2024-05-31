# 为什么不能用sliding window：因为nums中的元素有正有负，而two pointer/sliding window的原则为：
# 如果我知道大窗口的结果，就可以得到小窗口的结果，知道小窗口的结果也可以反推出大窗口的结果
# 而这里的结果是完全随机的
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(lambda: 0)
        count[0] = 1
        ans = 0
        total = 0
        for num in nums:
            total += num
            ans += count[total - k]
            count[total] += 1
        return ans


# 2024
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        hashmap = dict()
        total = 0
        hashmap[total] = 1
        
        for i in range(len(nums)):
            total += nums[i]
            if total - k in hashmap:
                count += hashmap[total - k]

            if total not in hashmap:
                hashmap[total] = 1
            else:
                hashmap[total] += 1
        
        return count