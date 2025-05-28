# all numbers divisible by 3 or 5 or 7:
# 3s + 5s + 7s - 15s - 21s - 35s + 105s
# explain: venn diagram
# 15 is overlap of 3 and 5
# 21 is overlap of 3 and 7
# 35 is overlap of 5 and 7
# then we add 105 (overlap of all three) back
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sumOfDivisible(value: int) -> int:
            low = value
            high = (n // value) * value
            count = (high + value - low) // value
            return (low + high) * count // 2

        return (
            sumOfDivisible(3)
            + sumOfDivisible(5)
            + sumOfDivisible(7)
            - (sumOfDivisible(15) + sumOfDivisible(35) + sumOfDivisible(21))
            + sumOfDivisible(105)
        )    