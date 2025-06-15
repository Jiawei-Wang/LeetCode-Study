class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        lookup = set()
        for number in arr:
            if number * 2 in lookup:
                return True
            if number % 2 == 0 and number // 2 in lookup:
                return True
            lookup.add(number)
        return False