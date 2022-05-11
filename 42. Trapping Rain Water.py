class Solution:
    def trap(self, height: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=ZI2z5pq0TqA&ab_channel=NeetCode 
        每个位置能储存的水量是该元素左右两侧最大元素的较小者与该元素的差值
        water = min(biggest_left_element, biggest_right_element) - height[i]
        所以该题就转化为：如何确定每个元素左右两侧的最大元素
        """
        
        # 解法1：三次遍历，time n space n
        if len(height) == 1 or len(height) == 2:
            return 0
        
        # find biggest left
        left = [0, height[0]] # 第一个元素的最大左元素为0, 第二个元素的最大左元素为第一个元素
        curr = max(height[0], height[1])
        for i in range(2, len(height)):
            left.append(curr)
            curr = max(curr, height[i])

        # find biggest right
        right = [height[-1], 0] # 最后一个元素的最大右元素为0，倒数第二个元素的最大右元素为最后一个元素
        curr = max(height[-1], height[-2])
        for i in range(len(height)-3, -1, -1):
            right.insert(0, curr)
            curr = max(curr, height[i])
        
        # find water
        ans = 0
        for i in range(len(height)):
            if min(left[i], right[i]) - height[i] > 0:
                ans += min(left[i], right[i]) - height[i]
            else:
                continue
        return ans
        

class Solution:
    def trap(self, height: List[int]) -> int:
        # 解法2：two pointer time n space 1
        if len(height) <= 2:
            return 0
        
        # 从左右两侧逐步向内遍历，每走一步更新该元素对应的水量
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        ans = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l] # 这两行写法很聪明，因为可以避免使用 >0? 的判断语句
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        return ans