class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        last_round = k % sum(chalk)
        i = 0
        while last_round >= 0:
            last_round -= chalk[i]
            if last_round < 0:
                return i
            else:
                i += 1
