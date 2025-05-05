# simulate every move: recursion + duplication
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        num_all_moves = 8 ** k
        positions = [(row, column)]
        next_positions = []

        def make_move(pos):
            r = pos[0]
            c = pos[1]
            for next in [(r+2,c+1),(r+1,c+2),(r-1,c+2),(r-2,c+1),(r+2,c-1),(r+1,c-2),(r-1,c-2),(r-2,c-1)]:
                if 0 <= next[0] < n and 0 <= next[1] < n:
                    next_positions.append((next[0],next[1]))
            
        for _ in range(k):
            for current in positions:
                make_move(current)
            positions = next_positions
            next_positions = []
        
        return len(positions)/num_all_moves


# simulate every move: recursion + better memory 
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        from collections import defaultdict

        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (2, -1), (1, -2), (-1, -2), (-2, -1)
        ]

        # current step position counts
        position_counts = {(row, column): 1.0}

        for _ in range(k):
            next_counts = defaultdict(int)
            for (r, c), count in position_counts.items():
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        next_counts[(nr, nc)] += count
            position_counts = next_counts

        return sum(position_counts.values()) / (8 ** k)


# dp
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        """
        think process:
        1. to improve upon recursion solution, we need to remove duplications
        2. a data structure can be used to store previous calculation
        3. it needs to store: current position on the board, how many moves left, and current possibility
        4. so a 3d array is needed to store the information
        """
        # dp[r][c][k] represent the probability that the knight remains 
        # on the board when starting at cell (r, c) with k moves remaining
        dp = [[[-1.0] * (K + 1) for _ in range(N)] for _ in range(N)]
        directions = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

        def find(N, K, r, c):
            # for current step, we first check if it's valid
            # If the knight moves off the board, this path contributes 0 probability
            if r < 0 or r >= N or c < 0 or c >= N:
                return 0
            
            # then check if it's the last step
            # If no moves remain and the knight is still on the board, 
            # this path contributes 1 (100%) to the probability
            if K == 0:
                return 1
            
            # if it's already calculated before
            # use the info directly
            if dp[r][c][K] != -1.0:
                return dp[r][c][K]
            
            # for a brand new step, the possibility depends on all 8 next steps
            poss = 0
            for dr, dc in directions:
                poss += 0.125 * find(N, K - 1, r + dr, c + dc)
            dp[r][c][K] = poss
            return poss

        return find(N, K, r, c)
        
        
