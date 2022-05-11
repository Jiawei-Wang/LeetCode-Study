class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r: # 最后一步可能只剩下一个元素，所以要用 <= 而不是 <
            m = l + (r-l)//2 # 防溢出
            if nums[m] > target:
                r = m-1 # m 本身已被排除，所以只需要从m的左边第一个元素开始继续寻找即可
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1