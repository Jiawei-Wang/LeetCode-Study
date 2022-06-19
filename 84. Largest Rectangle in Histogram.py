# 暴力解
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                area = max(area, (j-i+1)*min(heights[i:j+1]))
        return area


# https://www.youtube.com/watch?v=zx5Sw9130L0&ab_channel=NeetCode
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start,h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea
        