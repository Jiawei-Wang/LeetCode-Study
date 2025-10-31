class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for op in operations:
            if op[1] == "+":
                count += 1
            else:
                count -= 1
        return count