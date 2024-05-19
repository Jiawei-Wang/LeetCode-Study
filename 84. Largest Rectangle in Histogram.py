# 暴力解: calculate area for each subarray
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                area = max(area, (j-i+1)*min(heights[i:j+1]))
        return area


# for a bar i, the maximum rectangle's width is r-l-1
# l: the first coordinate of the bar to the left with height h[l] < h[i]
# r: the first coordinate of the bar to the right with height h[r] < h[i]
# and area = height[i] * (r-l-1)
# for example: [5, 7, 10, 5]
# for 7, the biggest area is 7 * 2
# so the simple way is to scan for r and l every time, in total: O(n^2)
# but we can reuse results of previous calculations and jump through indices with total O(n) 
class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        length = len(height)
        
        shorter_left = [-1] * length # idx of the first bar the left that is lower than current
        shorter_right = [length] * length # idx of the first bar the right that is lower than current

        for i in range(1, length):
            p = i - 1
            # use p >= 0 check first to prevent index out of range error
            while p >= 0 and height[p] >= height[i]: 
                p = shorter_left[p]
            shorter_left[i] = p

        """
        we know:
        1. p > i
        2. first element on the left to be < p is shorter_left[p]
        so anything between (shoter_left[p], p] >= p > i
        so we can start searching from shorter_left[p]
        """
        
        for i in range(length - 2, -1, -1):
            n = i + 1
            while n < length and height[n] >= height[i]:
                n = shorter_right[n]
            shorter_right[i] = n
        
        max_area = 0
        for i in range(length):
            max_area = max(max_area, height[i] * (shorter_right[i] - shorter_left[i] - 1))
        return max_area


# we go through all bars, each time we check if start/end index for this bar's maxArea can be found
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                """
                previous height > current height means two things:
                1. previous maxArea has a right end index now
                2. current maxArea has a left start index now
                """
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start,h))
        
        # for all left over ones (the ones with no right end index)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        
        return maxArea

        """
        for example: [2, 1, 5]
        we know: 
        for 2: start = 0, end = 0
        for 1: start = 0, end = 2
        for 5: start = 2, end = 2
        so when we go through this code: 
        1. go to 2, add (0, 2) to stack
        2. go to 1, 2 > 1 so we do two thingsL:
            1) we find maxArea for 2: maxArea = 2 * (1-0) = 2
            2) we know maxArea for 1 starts from index = 0 not 1
        3. go to 5, add (2, 5) to stack
        4. so now stack contains all start index with no end index
        5. for 5, we know maxArea = 5 * 1
        6. for 1, we know maxArea = 1 * 3
        """