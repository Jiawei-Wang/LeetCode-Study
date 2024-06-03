class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1]
        while rowIndex != 0:
            temp = [1]
            for i in range(len(answer)-1):
                temp.append(answer[i] + answer[i+1])
            temp.append(1)
            rowIndex -= 1
            answer = temp
        return answer
        