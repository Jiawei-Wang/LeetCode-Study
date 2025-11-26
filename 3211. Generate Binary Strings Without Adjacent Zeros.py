class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, prev: int, string: str, n: int):
        if len(string) == n:
            self.ans.append(string)
            return
        self.dfs(1, string + '1', n) 
        if prev == 1: # only strings end with "1" can continue with "0"
            self.dfs(0, string + '0', n)

    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        self.dfs(0, "0", n) # start with "0"
        self.dfs(1, "1", n) # start with "1"
        return self.ans