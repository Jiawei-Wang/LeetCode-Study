# 思考：有n对括号，也就意味着有n个左括号并排排列，然后找到位置将n个右括号插进去
# 举例：n=3，那么当前问题就可以转化为：在 0（1（2（3 中找到所有位置将 ））） 放进去
# 其中位置0不能放元素，位置1最多可以放1个，位置2最多可以放2个，位置3最多可以放3个，以此类推
# 进一步简化问题：将n个元素放入位置1~n中，每个位置可放的元素最大量为位置标号
# 举例：[1,2,3]中放3个元素，可能解为：[0,0,3], [1,0,2], [0,1,2], [1,1,1], [0,2,1]，正好是题目给的例子
# 先用decision tree做: 先决定在位置n里放多少个元素，然后决定在位置n-1里放多少个元素，直到不剩元素时获得一个解
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def decision(position, available, total, path):
            # position：当前在哪个位置（同时也是当前位置能放多少个右括号）
            # available：还剩多少个右括号可以用
            # total：此前轮次一共用了多少右括号
            # path：之前的轮次的决定
            
            if position == 0 and available == 0: 
                ans.append(path)
                return 
            
            maxNumber = min(position, available, n-total) # 本轮最多能用的数量
            
            # 本轮最少需要用的数量是 当前左括号总数 - 已用右括号总数
            # 比如(1(2(3 中如果我走到位置3（刚开始第一轮loop），当前一共1个左括号，0个已用右括号，所以至少用1个
            # 走到位置2，当前一共2个左括号（2和3），前面轮次一共用了k个右括号，所以这轮是2-k
            minNumber = max(0, 1 + n - position - total)
            
            for numThisLoop in range(maxNumber, minNumber-1, -1):
                decision(position-1, available - numThisLoop, total + numThisLoop, path+[numThisLoop])
        
        decision(n, n, 0, [])
        
        trueAns = []
        for item in ans:
            string = ''
            for i in item:
                string += '(' * i + ')'
            trueAns.append(string)
            
        return trueAns


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


# dp
# 和创建2d list，并让每个位置上保存所有当前string相比，下面的方法使用的space少很多
# 理解方式：每一轮寻找所有能够插入一对括号的位置
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
                # for example i = 3: 
                # j = 0, 1, 2
                # dp[3] (initially empty) will add the following combinations:
                # (dp[0]) + dp[2]: put () before everything in dp[2]
                # (dp[1]) + dp[1]
                # (dp[2]) + dp[0]: put () around everything in dp[2]
        print(dp)
        return dp[n]
    
    """
    以n=3为例，上面的dp输出内容为：
    [''], 
    ['()'], 
    ['()()', '(())'], 
    ['()()()', '()(())', '(())()', '(()())', '((()))']
    """