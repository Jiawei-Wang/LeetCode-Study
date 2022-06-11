# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 将相邻的node两两对调，不允许直接修改node的val
# corner case：奇数长度的linked list怎么办：最后一个node保持原位
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        start = dummy
        # 如果当前node已经是末尾，则返回head即可
        # 如果当前node后面还剩（至少）2个node，两者颠倒
        # 如果当前node后面还剩1个node，不用管它
        # 每次node步进2个位置
        while start and start.next:
            if start.next.next:
                first = start.next
                second = start.next.next
                end = start.next.next.next
                
                start.next = second
                second.next = first
                first.next = end
            start = start.next.next
            
        return dummy.next