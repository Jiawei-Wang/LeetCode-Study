class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right = sum(nums)
        left = 0

        answer = []
        for num in nums:
            right -= num
            answer.append(abs(left - right))
            left += num
        
        return answer

        