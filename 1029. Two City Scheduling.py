# greedy:
# 1. send everyone to city A
# 2. calculate the refund we can get by sending everyone to city B
# 3. send the people with most refund to city B
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        total = 0
        for a, b in costs:
            refund.append(b-a)
            total += a
        refund.sort()
        for i in range(len(costs)//2):
            total += refund[i]
        return total