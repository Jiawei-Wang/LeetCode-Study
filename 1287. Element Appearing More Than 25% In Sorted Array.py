class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = len(arr) / 4
        current = -1
        count = 0
        for num in arr:
            if num == current:
                count += 1
            else:
                current = num
                count = 1
            if count > target:
                    return num