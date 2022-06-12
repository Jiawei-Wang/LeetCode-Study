# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 理解题意：长度的定义为最左边的node和最右边的node之间的距离（中间有空node也算距离）
# 举例：
#         1
#     2      3
#  4    x  x    5
# 则第一行距离为1，第二行为2，第三行为4，返回最大值4 
#
# 思考：能不能找出某种方式，在遍历时直接给每个元素都进行label，然后直接用label来计算即可（长度 = 两个index之差 + 1）
# label必须包含两个信息，行数，以及此行的序号
# 观察：假如parent node是第i行第j个（全部从0开始），那么它的左child是第i+1行第j*2个，右child是第j*2+1个
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 题目限定至少1个node
        if not root.left and not root.right:
            return 1
        
        # 先把每个（存在的）node的位置记下来
        rootPosition = [0, 0]
        nodes = [rootPosition]
        maxLen = 1
        
        def helper(parentPosition, left, node):
            if not node:
                return 
            
            nodePosition = [parentPosition[0]+1, parentPosition[1]*2]
            if not left:
                nodePosition[1] += 1
            nodes.append(nodePosition)

            helper(nodePosition, True, node.left)
            helper(nodePosition, False, node.right)
            
        
        helper(rootPosition, True, root.left)
        helper(rootPosition, False, root.right)
        
        # [i,j]表示node在第i行第j个
        nodes.sort()
        base = nodes[0][1]
        for i in range(1, len(nodes)):
            if nodes[i][0] != nodes[i-1][0]:
                maxLen = max(maxLen, nodes[i-1][1] - base + 1)
                base = nodes[i][1]
        maxLen = max(maxLen, nodes[i][1] - base + 1) # 最后一行下面没有新的行数，所以要把这一行的长度和上一个循环得到的max再对比一次
        return maxLen
                
            
# BFS
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 0
        level = [(1, root)] # 初始化：只有root一个node，其位于此层的第1个
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1) # width是当前最大值（从第1层到上一层），和此层长度，二者的最大值
            cur = []
            for number, node in level:
                for kid in enumerate((node.left, node.right), 2*number):
                    if kid[1]:
                        cur.append(kid)
            level = cur
            # 上面6行代码可以用这一行代替
            # level = [kid for number, node in level for kid in enumerate((node.left, node.right), 2 * number) if kid[1]]
        return width
