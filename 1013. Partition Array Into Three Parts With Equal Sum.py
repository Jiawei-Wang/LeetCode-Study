class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False
        length = len(arr)
        target = total // 3

        first = 0
        current = arr[first]
        while current != target:
            first += 1
            current += arr[first]
            if first == length-2:  # only 1 element left
                return False
        
        second = first + 1
        current = arr[second]
        while current != target:
            second += 1
            current += arr[second]
            if second == length-1:
                return False
        
        return sum(arr[second+1:]) == target


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3:
            return False
        target = sum(arr)//3
        total = 0
        count = 0
        for element in arr:
            total += element
            if total == target:
                count += 1
                total = 0
        return count >= 3 # >3 means there is a segment with sum == 0
