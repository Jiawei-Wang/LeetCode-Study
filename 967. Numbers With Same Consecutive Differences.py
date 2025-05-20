class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = set([])

        def find_next(number, digit, length):
            if length == n:
                answer.add(number)
            else:
                small = digit - k
                if small >= 0:
                    find_next(number*10+small, small, length+1)
                big = digit + k
                if big <= 9:
                    find_next(number*10+big, big, length+1)

        for first in range(1, 10):
            find_next(first, first, 1)
        
        return list(answer)