class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        duplicate = n - 1 # the number that should appear twice
        pending = {x for x in range(1, n)}
        for num in nums:
            if num in pending:
                pending.remove(num)
            else:
                if num != duplicate:
                    return False
        
        return not pending
            



