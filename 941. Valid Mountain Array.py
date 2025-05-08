class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        increase = True

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] > arr[i-1] and not increase:
                return False
            elif arr[i] < arr[i-1] and increase:
                if i == 1:
                    return False
                else:
                    increase = False
        
        return not increase
        