class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [0 for _ in range(len(prices))]
        stack = []
        for index, price in enumerate(prices):
            while stack and stack[-1][1] >= price:
                prev = stack.pop()
                answer[prev[0]] = prev[1] - price
            stack.append([index, price])
        for item in stack:
            answer[item[0]] = item[1]
        return answer

