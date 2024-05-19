# for n elements, if there is no duplicate, total number of combinations is 2^n
# (1 to 2^0) empty set is the first subset
# (2^0+1 to 2^1) add the first element into subset from (1)
# (2^1+1 to 2^2) add the second element into subset (1 to 2^1)
# (2^2+1 to 2^3) add the third element into subset (1 to 2^2)
# ....
# (2^(n-1)+1 to 2^n) add the nth element into subset(1 to 2^(n-1))
# when there are duplicates, we treat them as special elements
# for example: we have two 5s, we can:
# 1. not pick it
# 2. pick one 5
# 3. pick two 5s
# so for this question: 
# we are given an array (a1, a2, a3, ..., an) with each of them appearing (k1, k2, k3, ..., kn) times
# the number of subset is (k1+1)(k2+1)...(kn+1)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]] # base case we pick no element
        for num, freq in collections.Counter(nums).items(): # for each element
            res_len = len(res)
            for i in range(1, freq+1): # for each frequency
                for r in res[:res_len]: # we create a new subset from existing subset and append to answer
                    res.append(r+[num]*i)
        return res