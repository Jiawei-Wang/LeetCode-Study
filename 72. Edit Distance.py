"""
Here is a thing that I need to find math proof to it:
The shorest distance by editing in random order is the same as by editing char by char
For example: intention, execution
1. random order: 
    remove t:           inention
    replace i with e:   enention
    replace n with x:   exention
    replace n with c:   exection
    insert u:           execution
2. char by char:
    change inten to execu by doing 5 replaces
"""

"""
Recrusion: 
    1) base case: word1 = "" or word2 = "" => return length of other string
    2) if word1[0] == word2[0] => recurse on word1[1:] and word2[1:]
    3) if word1[0] != word2[0] => recurse by inserting, deleting, or replacing
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            insert = 1 + self.minDistance(word1, word2[1:])
            delete = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word1[1:], word2[1:])
        
        return min(insert, replace, delete)


# recrusion with memo
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.dp = dict()
        return self.md(word1, word2, 0, 0)
    
    def md(self, word1, word2, i, j):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in self.dp:
            if word1[i] == word2[j]:
                ans = self.md(word1, word2, i + 1, j + 1)
            else: 
                insert = 1 + self.md(word1, word2, i, j + 1)
                delete = 1 + self.md(word1, word2, i + 1, j)
                replace = 1 + self.md(word1, word2, i + 1, j + 1)
                ans = min(insert, delete, replace)
            self.dp[(i, j)] = ans
        return self.dp[(i, j)]


# dp
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
                    
        return table[-1][-1]