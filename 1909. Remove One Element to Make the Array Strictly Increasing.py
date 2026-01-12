class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        deleted = False

        for i in range(1, len(nums)):
            # if curr is not strictly bigger than prev
            if nums[i-1] >= nums[i]:
                if deleted == True:
                    return False
                
                deleted = True
                # two cases: delete prev and keep curr or delete curr and keep prev
                # first case no change needed
                # second case:
                if i > 1 and nums[i-2] >= nums[i]:
                    nums[i] = nums[i-1]
        
        return True