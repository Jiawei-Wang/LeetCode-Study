class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i] will store the number of NEW people who learn the secret on day i.
        # We use size n + 1 so day matches the 1-based index directly.
        dp = [0] * (n + 1)
        
        # Day 1: Exactly 1 person discovers the secret.
        dp[1] = 1
        
        # Tracks the number of people who are actively sharing the secret on the current day
        active_sharers = 0
        
        # Simulate the secret spreading from Day 2 to Day n
        for i in range(2, n + 1):
            # 1. Add people who learned the secret 'delay' days ago (they become active today)
            if i - delay >= 1:
                active_sharers = (active_sharers + dp[i - delay]) % MOD
                
            # 2. Subtract people who learned the secret 'forget' days ago (they forget today)
            if i - forget >= 1:
                active_sharers = (active_sharers - dp[i - forget] + MOD) % MOD
            
            # 3. The number of new people who learn the secret today is equal to the active sharers
            dp[i] = active_sharers

        # At day n, the total number of people who know the secret are those
        # who discovered it within the window [n - forget + 1, n]
        # Anyone who discovered it before that has already forgotten it.
        total_knowers = 0
        for i in range(max(1, n - forget + 1), n + 1):
            total_knowers = (total_knowers + dp[i]) % MOD
            
        return total_knowers