# prefix sum
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p # the remainder is the target we want to get

        if target == 0:
            return 0

        # we need to find a subarray with sum(subarray) == target + p * k
        # so that after removing it, the rest of the array will be divisible by p
        # also we want the shorest subarry if multiple exist
        # so now the question becomes:
        # find the shortest subarray with sum(subarray) % p == target

        answer = len(nums) # start with the worst answer: the whole array
        
        # before we start iterating over the array: 
        cur = 0 # current (prefix sum % p)
        # because (a+b)%p == (a%p+b)%p
        # 1. cur can represent both current prefix sum and current prefix sum % p
        # 2. also in the iteration loop, we can mod as many times as we want
        remainder_index = { # cur: index
            0: -1 # cur is 0: before we even start the array (-1)
        }
        
        for i, n in enumerate(nums):
            cur = (cur + n) % p
            # so now we know the remainder of sum(num[:i+1])
            # we need to check the diff between it and target
            prefix = (cur - target + p) % p # cur - target might be negative so adding p to ensure it's positive
            # and check if the diff exists in the hashmap: meaning some sum(num[:j]) already has the diff 
            if prefix in remainder_index:
                length = i - remainder_index[prefix]
                answer = min(answer, length)
            # since we want the shorest subarray, we want to use the biggest index for each prefix
            remainder_index[cur] = i  
        
        return -1 if answer == len(nums) else answer


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        rewrite the above answer in my own words
        for example
        nums = [3, 1, 4, 2]
        p = 6
        meaning we want to remove a chunk of nums
        so that the rest of it is 6*k
        we can remove either [3,1] or [4], so we pick [4]

        in order to apply this question to long input nums and big p
        we need to think about computing the target
        in this case target = 4, we need a subarray which == 4 + 6*k
        
        checking all possible subarray means O(n^2)
        to make it faster, we can use hashmap
        so for each end, we can quickly check all starts

        hashmap to store prefix sum info
        so now when we arrive at a new index (the end)
        we check if there is a prefix sum (start) to help us build the required subarray
        and we can improve it by only storing the biggest index for each prefix sum
        """
        target = sum(nums) % p
        if target == 0: return 0

        answer = len(nums)
        cur = 0 
        idx = -1
        hashmap = {
            cur: idx
        }

        for index, value in enumerate(nums):
            cur = (cur + value) % p
            diff = (cur - target + p) % p
            if diff in hashmap:
                answer = min(answer, index - hashmap[diff])
            hashmap[cur] = index
        
        return -1 if answer == len(nums) else answer