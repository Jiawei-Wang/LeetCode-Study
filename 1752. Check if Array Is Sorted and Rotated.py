class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        # 1 non-decreasing array
        # or 2 non-decreasing array with first_array[0] >= second_array[-1]
        
        if nums[0] >= nums[-1]: 
            # check to see if 2 non-decreasing array
            curr = 0
            second = False
            for i in range(len(nums)):
                nxt = nums[i]
                if nxt < curr:
                    if second == True:
                        return False
                    second = True
                curr = nxt
            return True
        else:
            # check to see if 1 non-decreasing array
            curr = 0
            for i in range(len(nums)):
                nxt = nums[i]
                if nxt < curr:
                    return False
                curr = nxt
            return True