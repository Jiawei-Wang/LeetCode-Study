class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use set: time n space: n
        a = set()
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)
        return False