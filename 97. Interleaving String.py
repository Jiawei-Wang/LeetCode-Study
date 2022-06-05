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

