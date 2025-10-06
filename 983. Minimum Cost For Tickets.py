# dp
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


# less space dp
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        travel = set(days)
        dp = [0] * 30  # circular buffer for last 30 days

        first, last = days[0], days[-1]

        for i in range(first, last + 1):
            if i not in travel:
                dp[i % 30] = dp[(i - 1) % 30]
            else:
                dp[i % 30] = min(
                    dp[(i - 1) % 30] + costs[0],           # 1-day pass
                    dp[max(0, i - 7) % 30] + costs[1],     # 7-day pass
                    dp[max(0, i - 30) % 30] + costs[2]     # 30-day pass
                )

        return dp[last % 30]


# decision tree with queues
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        last7 = deque()   # store (day, cost_if_buy_7_day_here)
        last30 = deque()  # store (day, cost_if_buy_30_day_here)
        cost = 0

        for d in days:
            # Remove expired 7-day and 30-day passes
            while last7 and last7[0][0] + 7 <= d:
                last7.popleft()
            while last30 and last30[0][0] + 30 <= d:
                last30.popleft()

            # Push new possible costs if buying new 7-day or 30-day pass at this day
            last7.append((d, cost + costs[1]))
            last30.append((d, cost + costs[2]))

            # Update cost as the min of buying 1-day, using active 7-day, or using active 30-day
            cost = min(cost + costs[0], last7[0][1], last30[0][1])

        return cost
