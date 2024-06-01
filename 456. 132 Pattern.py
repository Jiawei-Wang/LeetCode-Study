# find subsequence s1, s2, s3 such that s1 < s3 < s2
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = float('-inf') # s3 starts as -inf so nothing will be < s3
        stack = []

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s3: # only when s3 is assigned a value
                return True # will this return True
            else:
                while stack and nums[i] > stack[-1]: # if we can find s2, s3 pair
                    s3 = stack.pop() # we then assign the value to s3
            stack.append(nums[i])
        
        return False