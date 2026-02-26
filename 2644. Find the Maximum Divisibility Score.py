class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        answer = float("inf")
        best = 0
        for divisor in divisors:
            score = len([num for num in nums if not num % divisor])
            if score > best:
                best = score
                answer = divisor
            elif score == best:
                answer = min(answer, divisor)
        return answer
        