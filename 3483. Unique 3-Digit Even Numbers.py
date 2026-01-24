class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = set()
        n = len(digits)

        for i in range(n):
            if digits[i] == 0:
                continue  # no leading zero
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 != 0:
                        continue  # must be even

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    res.add(num)

        return len(res)
