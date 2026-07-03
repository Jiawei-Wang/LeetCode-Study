"""
brute force: decision tree
imagine this is Alice's turn and she is looking at the remaining stones starting at index i, she can:
1. take 1 stone and Bob gets the rest starting at i+1
2. take 2 and Bob gets i+2
3. take 3 and Bob gets i+3
Whatever choice Alices makes, Bob will return his maximum net gain from that point forward
so Alice net gain = stones Alice takes - Bob's optimal net gain from the next index
from test case 2 we know:
players don't pick stones to gain maximum score on this turn
players pick stones to gain maximum score diff overall
"""
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        def get_max_relative_score(i):
            # Base case: no more stones left
            if i >= n:
                return 0
            
            # Choice 1: Take 1 stone
            take_1 = stoneValue[i] - get_max_relative_score(i + 1)
            
            # Choice 2: Take 2 stones (if available)
            take_2 = float('-inf')
            if i + 1 < n:
                take_2 = stoneValue[i] + stoneValue[i+1] - get_max_relative_score(i + 2)
                
            # Choice 3: Take 3 stones (if available)
            take_3 = float('-inf')
            if i + 2 < n:
                take_3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - get_max_relative_score(i + 3)
                
            # The current player will optimally choose the maximum net gain
            return max(take_1, take_2, take_3)
        
        # Alice starts at index 0
        alice_net_score = get_max_relative_score(0)
        
        if alice_net_score > 0:
            return "Alice"
        elif alice_net_score < 0:
            return "Bob"
        else:
            return "Tie"