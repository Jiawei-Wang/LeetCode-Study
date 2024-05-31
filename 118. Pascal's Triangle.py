class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        current = [1]
        answer.append(current)
        for i in range(1, numRows):
            nxt = [1]
            for j in range(1, len(current)):
                nxt.append(current[j-1]+current[j])
            nxt.append(1)
            answer.append(nxt)
            current = nxt
        
        return answer


        