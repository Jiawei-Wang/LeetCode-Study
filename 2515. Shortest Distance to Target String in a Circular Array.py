class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        shortest = n
        for i in range(n):
            word = words[i]
            if word == target:
                shortest = min(shortest, min(abs(startIndex - i), n - abs(startIndex - i)))
        return shortest if shortest != n else -1
        