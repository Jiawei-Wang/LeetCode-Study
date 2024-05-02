"""
对于题目的理解：
2d list中有多个1d list element，每个element有一个名字（不同element间可能有重名），以及多个email，重新整理这个2d list，
让同一个人的email全部收集在一起（同一个人的定义为：两个element拥有相同的email）

举例：
2d list = [
    [a, a1, a2],
    [a, a3, a4],
    [a, a2, a3],
    [b, b1, b2]
]
其中第0和第2个元素共享a2，第1和第2个元素共享a3，所以a这个人总共为：a1, a2, a3, a4
所以答案应该为：
[
    [a, a1, a2, a3, a4],
    [b, b1, b2]
]

一开始我的解法：
外层遍历所有可能的2个element组合对
内层遍历这2个element中所有可能的2个email组合对
如果有重复，则两个element融合
这个解法有两个问题：
1. 时间复杂度非常高
2. 对于上面的例子会出现错误：因为它顺序遍历时发现第0个element和第1个element没有重复email，认为两者属于两个人
"""


# DFS: https://leetcode.com/problems/accounts-merge/discuss/109161/Python-Simple-DFS-with-explanation!!!
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):
        # 1
        emails_accounts_map = defaultdict(list)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_accounts_map[email].append(i)
        
        
        visited_accounts = [False] * len(accounts)
        res = []
        
        # 3
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)
        
        # 2
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
    

"""
对于DFS答案的理解：
1. 首先创建一个dict，其中key为email，value为这个email出现过的所有element的下标
   依旧使用上面的例子，我们可以得到：
   dict = {
        a1: [0]
        a2: [0, 2]
        a3: [1, 2]
        a4: [1]
        b1: [3]
        b2: [4]
   }
2. 然后遍历每个element，将它的email放入一个新的list中，以list为起点开始DFS
3. DFS逻辑类似于数岛，从dict中找出所有相连element，并将这些element中的email再加入，直到所有element都被耗尽
（一次DFS的recursion可以保证同一个人的所有email都被加入进list）
"""


# Union Find
"""
对于class UF的理解：
1. 初始化获得一个parent list：[0,1,2,3,etc]，此时每个index对应的值和index相同，代表accounts中每个element的parent是它自己
2. find(x)：如果element的parent不是它自己，则recursion找到parent=自己的那个element并返回它（这个element是这个union的root）
3. union(child, parent)：更新union关系，让一个element（child）的parent指向另一个元素（parent）
"""
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        # 这个循环结束后，我们会获得一个dict，里面key为email，value为email对应的union中的parent
        ownership = {}
        for i, (name, *emails) in enumerate(accounts): # 学习这个提取出sublist的语法
            for email in emails:
                if email in ownership: # 如果ownership[email]已经被设定为某个element
                    uf.union(i, ownership[email])  # 将此轮的element在union的parent设为已存在的那个element
                ownership[email] = i # 如果这个email是第一次遇见，将ownership[email]设为此element
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            # union中的parent并不一定是root（比如 0 -> 1 -> 2)，我们知道1是2的parent，但这里我们需要的是0，所以调用find()
            ans[uf.find(owner)].append(email) 
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]


# 2024
class UF:
    # we use a list to reprent relationship
    # every element in the list represents an "element" in the given input
    # index is how we can access this element
    # value is the index of another element in the list, representing parent of current element
    # for example: [0, 1]: two elements, first element's parent is itself (index = 0, self.parents[index] = index), same for second element
    # [1, 1]: first element's parent is the second element, second element's parent is itself
    
    # initilize the relationship: everyone is its own parent
    def __init__(self, N):
        self.parents = list(range(N)) # a list: [0, 1, 2, ..., N-1]: self.parents[index] = index

    # merge two groups together
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent) # let the root of "child" points to the root of "parent"
    
    # find the root of a parent-child group (a group may have many paths)
    def find(self, x):
        if self.parents[x] != x: # if index and value are not the same (element x is not its own parent)
            self.parents[x] = self.find(self.parents[x]) # recursion till we find the element that is its own parent
            # during the recursion:
            # 1. current parent-child path is updated: all children on this path (not necessarily all children in this group)
               # point to the root directly
            # 2. which is reflected as value for this index in self.parents list is changed
            # so if we have [1, 2, 2]: 0 -> 1 -> 2, find(0) will change it to: [2,2,2] (both 0 and 1 are now direct childrend of 2)
        return self.parents[x] # return the element (which is the root of current parent-child group)
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        ownership = {}
        for i, (name, *emails) in enumerate(accounts): # 学习这个提取出sublist的语法
            for email in emails:
                if email in ownership: # if email already has an owner
                    uf.union(i, ownership[email]) # merge these two owners into one group
                ownership[email] = i # let account i owns this email (update either from None, or from previous owner)
        # when we finish this part, we have a dictionary ownership, which contains all emails and their owners
        # every email only has one owner as value (although it may in fact has multiple owners in the input)
        # we also have a owner relationship list, which has all owner groups
        
        ans = collections.defaultdict(list) # ans is a dictionary: key is the unique owner, value is a list of emails
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email) # we find the root of this child, and put the email into this root  
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
    