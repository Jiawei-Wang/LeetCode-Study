# 1.理解题目：复述，简单例子，询问corner case
# 2.告知所有能想到的DSA：复杂度，优缺点，讨论最优解
# 3.边写边讲：为什么用这个语法，询问是否可以用built in
# 4.检查：语法是否有误，corner case and test case brain storm，手算一遍代码


"""
思考：我们并不需要去考虑 abs(# of substrings(s1)) - # of substrings(s2)) <= 1的问题
     因为我们一直在轮流切换string，所以结尾时两个string的substring数量之差必然为0或者1
限制条件：1. 必须轮流切换string
         2. 每次切换完后必须至少走一个char
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # corner case
        if not s1 and not s2 and not s3:
            return True
        elif not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3
        
        l1 = len(s1)
        l2 = len(s2)
        # key: (index_s1, index_s2, string), value: True/False to get s3 from here 
        dp = dict()
        
        # 当前走到s1[i], s2[j]，组成的string，寻找下一步的char使用哪个string
        def helper(i, j, string): 
            # 当任意一个index走到头时，检查当前string是否满足条件
            if i == l1 and j == l2:
                if string == s3:
                    dp[(i,j,string)] = True
                else:
                    dp[(i,j,string)] = False
                return dp[(i,j,string)]
            elif i == l1 and j < l2:
                if string+s2[j:] == s3:
                    dp[(i,j,string)] = True
                else:
                    dp[(i,j,string)] = False
                return dp[(i,j,string)]
            elif i < l1 and j == l2:
                if string+s1[i:] == s3:
                    dp[(i,j,string)] = True
                else:
                    dp[(i,j,string)] = False
                return dp[(i,j,string)]
              
                
            if (i, j, string) in dp:
                return dp[(i, j, string)]
            
            dp[(i, j, string)] = helper(i+1, j, string+s1[i]) or helper(i, j+1, string+s2[j])
            
            return dp[(i,j,string)]
        
        
        return helper(0,0,'')
            
"""
上面答案是正确的，但是爆内存
"""


# 2024
"""
translate the question into DFS on graph:
1. question asks: to create s3 by switching between s1 and s2
2. so we can have a 2d grid, with chars from s1 as row and chars from s2 as col
3. we start from topleft and move either to the right or to the bottom
    1) to the right: we take a char from s2
    2) to the bottom: we take a cahr from s1
4. if we can reach bottomright, s3 can be formed
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l= len(s1), len(s2), len(s3)
        if r + c != l:
            return False

        stack, visited = [(0, 0)], set((0, 0))

        while stack:
            x, y = stack.pop()
            # for every position we are currently in, we have 3 options

            # 1. if it's already the bottomright
            # (only when x = r, y = c will x + y = l)
            if x + y == l:
                return True
            
            # 2. if we want to move down:
            #   1) we are currently standing within bound
            #   2) and this char matches the char we need
            #   3) and the one below (regardless if it's within bound or out of bound) is new 
            if x < r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y))
                visited.add((x+1, y))

            # 3. if we want to move to right
            if y < c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1))
                visited.add((x, y+1))

            """
            we want to move down != we can move down
            1. we need check if we can move down
            2. if we can move both down or to the right, we pick one
            3. so we dfs to see if we can find one valid path
            """

        return False


# DP 
# O(m*n) space
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l= len(s1), len(s2), len(s3)

        if r+c != l:
            return False
        
        dp = [[True for _ in range(c+1)] for _ in range(r+1)]
        # dp[i][j] = True: we can create s3[0: i+j] by using s1[0:i] and s2[0:j]
        # dp[0][0] = True

        for i in range(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
                (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1][-1]


# O(2*n) space
# because when we go through the grid, we go row by row
# so two rows are enough
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1)+1, len(s2)+1
        
        if l1 + l2 != len(s3) + 2:
            return False

        pre = [True for _ in range(l2)]
        for j in range(1, l2):
            pre[j] = pre[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, l1):
            # first create the new row
            cur = [pre[0] and s1[i-1] == s3[i-1]] * l2
            for j in range(1, l2):
                # then calculate the new row
                cur[j] = (cur[j-1] and s2[j-1] == s3[i+j-1]) or \
                        (pre[j] and s1[i-1] == s3[i+j-1])
            # last reassign the value
            pre = cur[:]

        return pre[-1]


# O(n) space
# because we use prev row to calculate curr row, and reassign curr to be prev
# we can also just do the calculation in place on prev alone
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [True for _ in range(c+1)] 
        for j in range(1, c+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, r+1):
            dp[0] = (dp[0] and s1[i-1] == s3[i-1])
            for j in range(1, c+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1]


# 2026
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        # what data structure
        dp[i][j] == True 
        meaning using the first i char from s1 and first j char from s2 can form first i+j char of s3
        s3[0: i+j] can be formed by using s1[0:i] and s2[0:j]

        # what problem
        check if dp[len(s1)][len(s2)] is True or False

        # what base case
        dp[0][0] = True: using 0 char from s1 and 0 char from s2 can form first 0 char of s3

        # what transition
        # each step we need to pick a char from either s1 or s2 so
        for dp[i][j]
        current char = s3[i+j-1] 
        if current char == s1[i-1] and dp[i-1][j] == True
        or current char == s2[j-1] and dp[i][j-1] == True
        dp[i][j] = True
        """

        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l3 != l1 + l2:
            return False

        if not l1:
            return s2 == s3
        if not l2:
            return s1 == s3
        
        if s3[0] != s1[0] and s3[0] != s2[0]:
            return False
        
        # s1 on col, s2 on row
        dp = [[False for _ in range(l1+1)] for _ in range(l2+1)]
        dp[0][0] = True
        
        for i in range(1, l1+1):
            # if we use only i chars from s1
            if s1[0:i] == s3[0:i]:
                dp[0][i] = True
        
        for j in range(1, l2+1):
            if s2[0:j] == s3[0:j]:
                dp[j][0] = True
        
        for j in range(1, l2+1):
            for i in range(1, l1+1):
                current_char = s3[i+j-1]
                if (current_char == s1[i-1] and dp[j][i-1] == True) or (current_char == s2[j-1] and dp[j-1][i] == True):
                    dp[j][i] = True
        
        return dp[-1][-1]




