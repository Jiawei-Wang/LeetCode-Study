class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        current = 0
        total = 0
        for row in bank:
            ones = row.count("1")
            if ones == 0:
                continue
            else:
                total += current * ones
                current = ones
        return total