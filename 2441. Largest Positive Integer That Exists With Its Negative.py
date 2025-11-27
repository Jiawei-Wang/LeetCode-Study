class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        answer = -1
        for num in nums:
            seen.add(num)
            if -num in seen:
                answer = max(answer, abs(num))
        return answer
        