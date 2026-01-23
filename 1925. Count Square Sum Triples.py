class Solution:
    def countTriples(self, n: int) -> int:
        # a, b, c are all in [1, n] range (inclusive)
        upperbound = n * n 
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c_sq = a * a + b * b
                if c_sq <= upperbound and int(math.sqrt(c_sq)) * int(math.sqrt(c_sq)) == c_sq:
                    count += 1
        return count
