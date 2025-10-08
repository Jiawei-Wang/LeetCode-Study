# https://leetcode.com/problems/put-marbles-in-bags/solutions/3111642/simple-c-solution-using-sort-idea-explained
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        if k == 1 or k == n:
            return 0

        candidates = [weights[i] + weights[i + 1] for i in range(n - 1)]
        candidates.sort()
        
        mins = sum(candidates[:k-1])
        maxs = sum(candidates[-(k-1):])
        
        return maxs - mins