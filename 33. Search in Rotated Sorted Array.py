class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 在一个被rotate过的sorted list中寻找目标元素的下标
        
        # 先花logn找到断点，再花logn找到元素下标
        # 不行，难点一：要拿mid和前后元素对比，需要反复验证前后元素是否越界
        # 难点二：如果nums[mid-1] < nums[mid] < nums[mid+1]，仍然不知道mid到底在断点前还是断点后
        
        # 分情况讨论即可
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]: # 说明 l~mid 这一段是单调递增的连续sublist
                if target > nums[mid] or target < nums[l]: # 两种情况均说明target在右侧
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else: # 说明 mid~r 这一段是单调递增的连续sublist
                if target < nums[mid] or target > nums[r]: # 两种情况均说明target在左侧
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
            