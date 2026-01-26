class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        cnt = Counter(s)

        if len(cnt) <= k:
            return 0

        freqs = sorted(cnt.values())
        remove = len(freqs) - k
        return sum(freqs[:remove])
