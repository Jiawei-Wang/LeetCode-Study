# 解法1: 暴力解
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                ans = max(ans, area)
        return ans


# 解法2: two pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 首尾两端
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water