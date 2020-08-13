"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# DFS
class Solution:
    def getImportance(self, employees: List['Employee'], query_id: int) -> int:
        # 学习这种快速初始化dictionary的方法
        emap = {e.id: e for e in employees}

        # 学习这种使用sub function的方法
        def dfs(eid):
            employee = emap[eid]
            # 学习这种获得子Employee总权重的方法
            return employee.importance + sum(dfs(eid) for eid in employee.subordinates)

        return dfs(query_id)


# 此答案应该是对的，没有编译错误，但是提示超时
# BFS
from queue import Queue
class Solution:
    def getImportance(self, employees: List['Employee'], query_id: int) -> int:
        emap = {e.id: e for e in employees}
        queue = Queue()
        queue.put(emap[query_id])
        total = 0

        while queue:
            current = queue.get()
            total += current.importance
            for subordinate in current.subordinates:
                queue.put(emap[subordinate])

        return total
