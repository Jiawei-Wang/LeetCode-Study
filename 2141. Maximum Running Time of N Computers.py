# ideally we want to use all batteries evenly
# so no energy left unused
# so best case possible is sum(batteries) / n minutes
# this is the upperbound
# 
# if a battery has too much energy, in that case some energy may be wasted
# if a battery has too little energy, it will always be fully used
# 
# for a batter with too much energy: max(batteries)
# if max(batteries) > sum(batteries) / n:
# then this battery can be used for charging all the time, without being unplugged
# so now the problem becomes rest of the batteries and n-1 computers
#
# keep doing the above process till max(batteries) <= sum(batteries) / n
# that means all rest of batteries can be fully used
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total = sum(batteries)
        while batteries[-1] > total / n:
            n -= 1
            total -= batteries.pop()
        return total // n