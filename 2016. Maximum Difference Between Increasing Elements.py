class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -1
        cur_min = nums[0]

        for num in nums[1:]:
            if num > cur_min:
                answer = max(answer, num - cur_min)
            else:
                cur_min = num
        
        return answer