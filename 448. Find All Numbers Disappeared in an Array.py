class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = set(x for x in range(1, len(nums)+1))
        for num in nums:
            if num in answer:
                answer.remove(num)
        return list(answer)