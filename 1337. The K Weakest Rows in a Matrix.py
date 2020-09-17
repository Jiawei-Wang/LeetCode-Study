# 读题理解:
# 1. 题目要求: 将所有的row按照 1 的数量进行从小到大排序, 输出前 k 个row的下标
# 2. 限制: 1. 每个row的所有 1 都在前面, 0 在后面; 2. 当两个row的 1 的数量相同时, 下标小者顺序在前

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # i是每row的下标, g是row这个array本身
        # S是一个2d array, 每一行是 [1的数量, row的下标]
        S = [[sum(g),i] for i,g in enumerate(mat)]
        
        # 从小到大排列
        R = sorted(S)
        
        # 输出下标组成的array
        return [r[1] for r in R[:k]]


# one line with heap
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the iterable specified and satisfying the key if mentioned
        return [r[1] for r in heapq.nsmallest(k,[[sum(g),i] for i,g in enumerate(mat)])]