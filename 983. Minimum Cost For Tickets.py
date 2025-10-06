class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel = set(days) # for faster lookup
        dp = [0] * 366  # dp[i] = min cost to cover up to day i

        for i in range(1, 366):
            if i not in travel:
                dp[i] = dp[i - 1]  # no travel today, same cost
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],          # 1-day pass
                    dp[max(0, i - 7)] + costs[1],  # 7-day pass
                    dp[max(0, i - 30)] + costs[2]  # 30-day pass
                )
        return dp[365]
