"""
from simulation (smashing rocks) to partitioning (knapsacks) to dp:

when you smash two rocks a and b (a >= b)
you are left with a new rock a - b 
if you keep doing this till there is 1 or 0 rock remaining
you are essentially assigning a positive or negative sign to every stone in the original set
for example for 4 stones a, b, c, d
one possible outcome is:
(a + b) - (c + d):
    smash a and c to get (a - c), if a >= c
    smash b and d to get (b - d), if b >= d
    then smash (a - c) and (b - d) to get a - c - b + d, if (a - c) >= (b - d)
and all other possible outcomes can be represented using positive and negative signs for each number as well
for example maybe a is very big, then one outcome would be a - b - c - d
so now it's a decision tree problem, for n rocks, we need to figure out which sign to use

the ultimate goal is to have the smallest rock leftover
if we knew the best way to partition rocks into two groups
g1 for positive sign and g2 for negative sign
then the difference beteen sum(g1) and sum(g2) should be minimized almong all possible partitions

diff = sum1 - sum2 
     = (total_sum - sum2) - sum2 
     = total_sum - 2 * sum2

so we want to get sum2 as close to total_sum/2 as possible

now the problem is:
find a subset of stones whose sum is as close to total_sum/2 as possible
and this is 0/1 knapsack problem
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        
        # dp[i] = True if a sum of 'i' can be achieved with a subset of stones
        dp = [False] * (target + 1)
        dp[0] = True
        
        for stone in stones:
            # Iterate backwards to ensure each stone is used only once (0/1 Knapsack)
            for weight in range(target, stone - 1, -1):
                if dp[weight - stone]:
                    dp[weight] = True
        
        # Find the largest achievable sum 'i' that is <= target
        for i in range(target, -1, -1):
            if dp[i]:
                # The two piles are 'i' and 'total_sum - i'
                # The difference is (total_sum - i) - i
                return total_sum - 2 * i
                
        return 0