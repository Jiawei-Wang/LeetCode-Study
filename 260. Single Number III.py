class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        check = set()
        for element in nums:
            if element not in check:
                check.add(element)
            else:
                check.remove(element)
        return list(check)