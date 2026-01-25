class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed_once = int(str(num)[::-1])
        reversed_twice = int(str(reversed_once)[::-1])
        return reversed_twice == num


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
            
        return str(num)[-1] != "0"
        