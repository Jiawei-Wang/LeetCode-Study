class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                if j == i: 
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    a, b, c = digits[i], digits[j], digits[k]

                    # Hundreds digit cannot be zero
                    if a == 0:
                        continue

                    # Last digit must be even
                    if c % 2 != 0:
                        continue

                    num = 100*a + 10*b + c
                    result.add(num)

        return sorted(result)
