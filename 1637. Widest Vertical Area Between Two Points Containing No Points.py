class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        array = [point[0] for point in points]
        array.sort()
        answer = 0
        for i in range(len(array)-1):
            answer = max(answer, array[i+1]-array[i])
        return answer
