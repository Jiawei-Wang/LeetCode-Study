# all num in nums are unique, find target num, if it exists return index, else return -1

# answer 1: use low as return value 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first pick value range
        # range is every possible index, but won't be -1 or len(nums)
        low = 0
        high = len(nums)-1

        # second pick stop sign
        while low < high: 
            # third pick mid 
            mid = low + (high-low)//2

            # fourth pick range
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid # because mid is not excluded in next loop, we need while low < high to prevent endless loop

        """
        1. all elements can be possible answer, so index range is full
        2. we want to use low as return answer so low and high have to be the same value when we return (only 1 left)
        3. we pick middle/middle-left (so in case 2 elements left, low will be picked as new mid)
        4. we don't exlucde mid in the next loop, so in order to reduce from 2 to 1: we have to move low away from mid 
           (to prevent endless loop, otherwise if low is still mid, we got stuck)
        4. because low can only move if mid < target (not mid <= target), we do so 
        5. only 1 element is stop sign so we use while low < high instead of while low <= high (to prevent endless loop)
        """

        return low if nums[low] == target else -1


# answer 2: still use low, but with different loop
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high-low+1)//2 # if we use higher mid instead of lower mid, then we need to move high away from mid
            if nums[mid] > target: # so we change mid < target to mid > target
                high = mid - 1
            else:
                low = mid
        return low if nums[low] == target else -1


# anwer 3: still use low, but this time with one extra loop 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) -1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target: # we exclude mid in next loop so we need lo <= hi for finally check
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        # we dont need this anymore: return lo if 0 <= lo <= len(nums) - 1 and nums[lo] == target else -1
        # because return lo if 0 <= lo <= len(nums) - 1 and nums[lo] == target is handled in last loop when lo == hi
        return -1 