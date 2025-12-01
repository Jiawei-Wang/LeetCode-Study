class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        longest = horizontalCuts[0] - 0
        for i in range(1, len(horizontalCuts)):
            longest = max(longest, horizontalCuts[i]-horizontalCuts[i-1])
        longest = max(longest, h-horizontalCuts[-1])

        widest = verticalCuts[0] - 0
        for i in range(1, len(verticalCuts)):
            widest = max(widest, verticalCuts[i]-verticalCuts[i-1])
        widest = max(widest, w-verticalCuts[-1])

        return (longest * widest) % (10**9 + 7) 

