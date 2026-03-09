# any integer target (positive or negative) is reachable by adding or subtracting a prefix of natural numbers (1, 2, 3, ...., n):
# 1. find the smallest k such that sum(1, 2, 3, ..., k) >= abs(target)
# 2. check the difference D = sum - abs(target)
# 3. if D is even: I just need to find a number i in the sum such that 2*i == D, flip the sign of i
# 4. if D is odd: keep adding the next numbers (k+1, k+2, ...) till D is even
class Solution:
    def reachNumber(self, target: int) -> int:
        # so going back to this question, now to find steps to get target
        target = abs(target)
        step = 0
        total = 0

        # 1.
        while total < target: 
            step += 1
            total += step

        # 2. 3. 4.
        while (total - target) % 2 != 0:
            step += 1
            total += step
        
        return step