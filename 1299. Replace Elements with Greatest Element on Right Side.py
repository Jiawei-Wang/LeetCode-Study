class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        if length == 1:
            return [-1]
        cur_max = arr[-1]
        arr[length-1] = -1
        for i in range(length-2, -1, -1):
            arr[i], cur_max = cur_max, max(cur_max, arr[i])
        
        return arr
        