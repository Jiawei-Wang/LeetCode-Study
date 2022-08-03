"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# 难点：无法在遍历linked list时实时建立node之间的关系
# 解决办法：先使用一个数据结构将所有node的指针都暂时保存起来
# 使用hashmap来实现最短读取速度
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}
        
        # 第一次遍历创建新node（只包含val的信息），新老node保存进hashmap
        cur = head
        while cur:
            copy = Node(cur.val)
            hashmap[cur] = copy
            cur = cur.next
            
        # 第二次遍历：将新node互相串联起来
        cur = head
        while cur:
            copy = hashmap[cur]
            copy.next = hashmap[cur.next]
            copy.random = hashmap[cur.random]
            cur = cur.next
            
        return hashmap[head]