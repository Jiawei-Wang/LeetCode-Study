# 暴力解：先生成2^(2n)个string，然后挨个检查哪个符合要求
# time: 2^(2n)*n，因为验证也需要O(n)，space: 2^(2n)*n，因为每个string占n个位置
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def legit(string):
            # 合法的string需要满足两个条件：1.左括号先于右括号，2.左括号和右括号一样多
            # "先于"这个条件不好implement，所以可以使用下面的方法
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        pairs = []
        def helper(string, length):
            if length == 2*n:
                if legit(string):
                    pairs.append(string)
                return
            helper(string+'(', length+1)
            helper(string+')', length+1)
        helper('', 0)
        return pairs


"""
对于题目的思考：
其实这个问题可以用图形来做对比：
1. 假设有两个stack，长度都为n，那么保证其中一个的当前元素数量永远不多于另一个
2. 假设有一个2d list，长宽为n，那么从左上角往右下角走保证一直在右上半边即可

所以可以：dp，backtrack，dfs等
"""


# dp
# 和创建2d list，并让每个位置上保存所有当前string相比，下面的方法使用的space少很多
# 理解方式：每一轮寻找所有能够插入一对括号的位置
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                # 若n=2，则所有(i,j)组合为[(1,0), (2,0), (2,1)]
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
    
    """
    以n=3为例，上面的dp输出内容为：
    ['()']
    ['()()']
    ['()()', '(())']
    ['()()()', '()(())']
    ['()()()', '()(())', '(())()']
    ['()()()', '()(())', '(())()', '(()())', '((()))']
    """
    
    """
    上面答案不是特别明白，还要再看看
    """


    # dfs
    class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        left = n
        right = n
        ans = []
        
        def dfs(left, right, ans, string):
            if right < left:
                return
            if not left and not right:
                ans.append(string)
                return
            if left:
                dfs(left-1,right,ans,string+"(")
            if right:
                dfs(left,right-1,ans,string+')')
        
        dfs(left,right,ans,'')
        return ans