# pigeonhole principle: 
# we start from 1 % k, then 11 % k, then 111 % k, ..., last one is k '1's % k
# first one to have 0 remainder is the answer
# if none has 0 as remainder, then within these numbers there must be at least 1 duplicate
# (because the possible remainders are from 1 to k - 1 and we have tried k different numbers)
# then we will never have a number divisible by k
# (because next_mod = (10* prev_mod + 1) % k, every next mod is determined by previous ones,
#  so eventually they will form a loop, and we have proven that there is no 0 in the loop)
# example: k = 6
# since 1111 % 6 = 1, we can directly calculate the remainder of 11111 % 6 using the formula above 
# 11111 % 6 = 5
# and the whole loop is:
# 1 % 6 = 1
# 11 % 6 = 5
# 111 % 6 = 3
# 1111 % 6 = 1
# 11111 % 6 = 5
# 111111 % 6 = 3
# so no answer for k = 6
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # 2, 4, 5, 6, 8 won't have any answer
        if k % 10 not in {1, 3, 7, 9}: 
            return -1

        mod, mod_set = 0, set()
        for length in range(1, k + 1):
            mod = (10 * mod + 1) % k
            if mod == 0: 
                return length
            if mod in mod_set: 
                return -1
            mod_set.add(mod)
            
        return -1
        