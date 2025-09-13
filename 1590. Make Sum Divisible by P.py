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
