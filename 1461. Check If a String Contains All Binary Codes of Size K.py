class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        length = len(s)
        hashset = set()
        for i in range(k, length+1):
            window = s[i-k: i]
            hashset.add(window)
            if len(hashset) == 2**k:
                return True
        return False
