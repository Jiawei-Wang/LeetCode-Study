class Solution:
    def minElement(self, nums: List[int]) -> int:
        def get_sum(num):
            string = str(num)
            return sum(int(digit) for digit in string)

        answer = float("inf")
        for num in nums:
            answer = min(answer, get_sum(num))
        return answer