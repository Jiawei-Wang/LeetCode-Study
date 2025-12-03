class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # try all first two number pairs
        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]
                
                # number can't have leading 0
                if b != str(int(b)):
                    continue
                
                while j < n:
                    c = str(int(a) + int(b))

                    if not num.startswith(c, j):
                        break
                    
                    j += len(c)
                    a, b = b, c
                
                # we just need one successful pair
                if j == n:
                    return True
        
        return False