class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        answer = n
        strike = 0
        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                strike += 1
                answer += strike
            else:
                strike = 0
        return answer