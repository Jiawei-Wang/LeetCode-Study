# find a palindrome prefix then do recursion on suffix
# for example: abacddcf
# a is a palindrome, so we do the same on bacddcf
# aba is a palindrome, so we do the same on cddcf
class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        """
        for each loop:
            1. return value is a 2d list
            2. we want to find all possible palindrome in current loop
                1) for example we have two palindromes
                2) we have palindrome A, suffix has 2 palindromes a1 and a2
                3) we have palindrome B, suffix has 1 palindrome b1
                4) then answer for current loop should be [[A+a1], [A+a2], [B+b1]]
        """
        if not s: 
            return [[]] # if s is empty, we return a list with only one sublist: []    
        ans = []
        # if s only contains one char, we return a list with only one sublist: [char]
        # if s contains more than one char, we return a list of [s[:i]] + suf
        for i in range(1, len(s) + 1): # for all possible prefix
            if s[:i] == s[:i][::-1]:  # if prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)

        return ans


# @cache keyword in last answer acts in the same way as DP
# DP: 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # first find all palindromes so we can do quick lookup
        palindrome = [[False] * n for _ in range(n)] # palindrome[i][j] will be True if s[i:j+1] is a palindrome
        for i in range(n):
            palindrome[i][i] = True  # Single characters are palindromes
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or palindrome[i + 1][j - 1]:
                        palindrome[i][j] = True
        
        # then dp through all combinations
        dp = [[] for _ in range(n + 1)] # dp[i] will store the palindrome partitions for substring s[i:]
        dp[n] = [[]]  # Base case: empty string has one partition: an empty list
        for i in range(n - 1, -1, -1): 
            for j in range(i, n):
                if palindrome[i][j]:
                    for partition in dp[j + 1]:
                        dp[i].append([s[i:j + 1]] + partition)
        
        return dp[0]


# same DP, but start from prefix instead of suffix
class Solution:
    def partition(self, s):
        n = len(s)

        palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            palindrome[i][i] = True  
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or palindrome[i + 1][j - 1]:
                        palindrome[i][j] = True
        
        dp = [[] for _ in range(n + 1)]
        dp[0] = [[]]
        for i in range(1, n + 1):
            for j in range(i):
                if palindrome[j][i - 1]:
                    current_partition = s[j:i]
                    for partition in dp[j]:
                        dp[i].append(partition + [current_partition])
        
        return dp[n]