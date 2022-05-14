class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # total cost for step[i] = min(total cost for step[i-1], total cost for step[i-2]) + cost[i]
        total = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            curr = min(total[i-1], total[i-2])+cost[i]
            total.append(curr)
        return min(total[-1], total[-2])


# recursion
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(cost, n):
            if not n or n == 1:
                return cost[n]
            return cost[n] + min(helper(cost, n-1), helper(cost, n-2))
        
        n = len(cost)
        return min(helper(cost, n-1), helper(cost, n-2))


