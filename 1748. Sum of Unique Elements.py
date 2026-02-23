class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        once = set()
        more = set()
        for num in nums:
            if num not in once and num not in more: # if new number
                once.add(num)
            elif num in once: # if second time
                once.remove(num)
                more.add(num)
            # if third time or more: do nothing
    
        return sum(once)