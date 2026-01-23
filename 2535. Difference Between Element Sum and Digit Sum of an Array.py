class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def get_sum(num):
            total = 0
            while num:
                digit = num % 10
                num = num // 10
                total += digit
            return total

        element_sum = sum(nums)
        digit_sum = sum([get_sum(num) for num in nums])
        return abs(element_sum - digit_sum)