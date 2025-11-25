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


# only use one stack
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        for i, value in enumerate(heights):
            while stack and heights[stack[-1]] < value: # people in front of current person && are shorter than current person: they will not see people behind current person
                res[stack.pop()] += 1
            if stack: # people in front of current person && are taller than current person: they are still in stack
                res[stack[-1]] += 1
            stack.append(i)
        return res