class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # question is equal to: who is closer to target, pacman or ghost
        x, y = target
        d = abs(x) + abs(y)
        return all(d < abs(x - i) + abs(y - j) for i, j in ghosts)