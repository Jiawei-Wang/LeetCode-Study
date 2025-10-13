class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        answer = []
        
        if length != m * n:
            return answer 

        for i in range(0, length, n):
            answer.append(original[i:i+n])
        
        return answer