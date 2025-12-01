class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        left = 0

        for i in range(1, len(colors)):
            if colors[i] != colors[left]:
                if i - left > 1:
                    answer += sum(neededTime[left:i]) - max(neededTime[left:i])
                left = i

        # handle the last group
        if len(colors) - left > 1:
            answer += sum(neededTime[left:]) - max(neededTime[left:])

        return answer
