class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pending = {x for x in range(0, n - 1)}
        answer = []
        for num in nums:
            if num in pending:
                pending.remove(num)
            else:
                answer.append(num)
        return answer