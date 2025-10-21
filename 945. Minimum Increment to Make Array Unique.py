# sorting nlogn
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0

        for i in range(1, len(nums)):
            # if current number is bigger than previous number, we do nothing
            # if current number is equal to previous number, current number += 1
            # if current number is smaller than previous number, 
            # which means we have used this number already, 
            # we need to bump this number to previous number + 1
            # for example [1, 2, 2, 3, 3]
            # [1, 2] are good, nothing needs to be done
            # second 2 needs to be bumped to 3
            # first 3 needs to be bumped to 4
            # second 3 needs to be bumped to 5
            if nums[i-1] >= nums[i]:
                answer += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        
        return answer