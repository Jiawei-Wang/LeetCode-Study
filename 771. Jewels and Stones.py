class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 暴力解：
        return sum(s in J for s in S)

        # Hashset
        setJ = set(J)
        return sum(s in setJ for s in S)
