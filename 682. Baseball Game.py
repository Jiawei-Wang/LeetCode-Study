class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array = []
        for op in operations:
            if op == "C":
                array.pop()
            elif op == "+":
                array.append(array[-1]+array[-2])
            elif op == "D":
                array.append(array[-1]*2)
            else:
                array.append(int(op))
        return sum(array)
        