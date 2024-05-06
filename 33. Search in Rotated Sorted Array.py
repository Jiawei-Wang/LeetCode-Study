# 在一个被rotate过的sorted list (with distinct values) 中寻找目标元素的下标
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                # if we get lucky, we find target, return mid
                # or we have only 1 element left (we are at the last loop where l = mid = r, we return mid or -1) 
                return mid

            # now we know nums[mid] is not what we are looking for
            # we need to look into l to mid and mid to r
            # binary search can only be used on ascending subarray
            # so we can only use binary search on two possibilities: 
            # 1. l to mid is ascending (not sure about mid to r)
            # 2. mid to r is ascending (not sure about l to mid)
            # and luckily, for a rotated subarray, wherever mid is, at least one possibility always satisfies
            # both satisfy if current subarray is ascending as a whole 

            elif nums[l] <= nums[mid]:
                # 说明 l~mid 这一段是单调递增的连续sublist
                # or we have two elements left and mid is currently pointing at l (l = mid = r - 1)  
                if target > nums[mid] or target < nums[l]: # 两种情况均说明target在右侧
                    l = mid + 1
                else: # nums[l] <= target < nums[mid] (we already know target != nums[mid])
                    r = mid - 1

                # if l = mid = r -1, after loop, we only have one possibility:
                # l = mid + 1, enter last loop to check if the last available element satisfies
                # r = mid - 1 is impossible (since we know l = mid, nums[l] <= target < nums[mid] is impossible)

            else: 
                # 说明 mid~r 这一段是单调递增的连续sublist with at least 3 elements
                # we have two elements left is impossible (in that case we should go into nums[l] <= nums[mid])
                if target < nums[mid] or target > nums[r]: # 两种情况均说明target在左侧
                    r = mid - 1
                else: # nums[mid] < target <= nums[r] (we already know target != nums[mid])
                    l = mid + 1

        return -1
            