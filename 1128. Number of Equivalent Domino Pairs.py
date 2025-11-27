class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        lookup = defaultdict(int)
        for domino in dominoes:
            small = min(domino)
            big = max(domino)

            lookup[(small, big)] += 1
        
        pair = 0
        for key, value in lookup.items():
            if value >= 2:
                pair += value * (value - 1) // 2
        return pair