# sliding window cannot be used in this question since num can be any integer 
# so when right index finds a subarray, we don't know whether to move right index or left index
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


# improve upon above solution 
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
