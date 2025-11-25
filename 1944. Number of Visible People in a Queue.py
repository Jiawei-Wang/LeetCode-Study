# brute force: create a monotonic increasing stack for every person
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = []
        for start in range(0, len(heights)): # for every person
            stack = []
            for index in range(start+1, len(heights)): # exam people behind this person
                if not stack or stack[-1] < heights[index]:
                    stack.append(heights[index])
                    if heights[index] > heights[start]: # if someone is taller than this person
                        break # we don't need to exam people behind them anymore
            answer.append(len(stack))
        return answer