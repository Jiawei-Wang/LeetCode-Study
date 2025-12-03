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



# 2025 
# dp
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        candidate_num = len(costs)
        dp_length = candidate_num//2+1

        dp = [[0 for _ in range(dp_length)] for _ in range(dp_length)]
        # dp[i][j] = k: if we assign i people to city A and j people to city B, the minimum cost is k
        # dp[0][0] = 0: base case

        # build the first row and first column
        row_sum = 0
        for i in range(1, dp_length):
            row_sum += costs[i-1][1]
            dp[i][0] = row_sum  
        col_sum = 0
        for j in range(1, dp_length):
            col_sum += costs[j-1][0]
            dp[0][j] = col_sum

        for i in range(1, dp_length):
            for j in range(1, dp_length):
                dp[i][j] = min(dp[i-1][j] + costs[i+j-1][1], dp[i][j-1] + costs[i+j-1][0])
        
        return dp[-1][-1]

