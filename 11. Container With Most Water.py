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


# 05-09-2022
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # # 暴力解
        # size = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         area = (j-i)*min(height[i], height[j])
        #         size = max(size, area)
        # return size
        
        # 优化 time n
        # 核心思路：将n^2个可能组合中必定不会是最优解的部分给排除在for loop外以实现O(n)
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        answer = 0
        while left != right:
            curr = (right - left) * min(height[left], height[right])
            answer = max(answer, curr)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        
        return answer