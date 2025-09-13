class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        hashset = set()
        i = -1
        for char in boxes:
            i += 1
            if char == "1":
                hashset.add(i)
        
        answer = []
        for i in range(len(boxes)):
            dis = 0
            for val in hashset:
                dis += abs(val - i)
            answer.append(dis)
        
        return answer


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        example:    11010
        leftCount:  01223   <- how many balls on my left
        leftCost:   01358   <- how much it costs to move all left side balls to me
        rightCount: 21100
        rightCost:  42100
        totalCost:  43458  
        """
        n = len(boxes)
        ans = [0] * n
        leftCount, leftCost, rightCount, rightCost = 0, 0, 0, 0
        for i in range(1, n):
            if boxes[i-1] == '1': 
                leftCount += 1
            leftCost += leftCount
            ans[i] = leftCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1': 
                rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans


        