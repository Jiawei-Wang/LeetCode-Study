class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        
        def find_length(num1, num2):
            length = 2
            while num1 + num2 in arr_set:
                num1, num2 = num2, num1+num2
                length += 1
            return length if length >= 3 else 0

        best = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                best = max(best, find_length(arr[i], arr[j]))
        return best