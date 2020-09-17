# 读题理解:
# 1. 题目要求: 将所有的row按照 1 的数量进行从小到大排序, 输出第 k 的row的下标
# 2. 限制: 1. 每个row的所有 1 都在前面, 0 在后面; 2. 当两个row的 1 的数量相同时, 下标小者顺序在前

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 先把每一row的 1 的数量找出来, 放进一个新的