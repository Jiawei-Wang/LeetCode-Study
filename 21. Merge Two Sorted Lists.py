# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 两个作用： 1. 和iterative中 cur.next = l1 or l2相同，将剩余部分连接上，2. 在刚开始时检查l1和l2是否存在，避免corner case
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2) # 将l1.next设为下一层循环中的返回值
            return l1 
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


# iterative
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # use a dummy head
        dummy = cur = ListNode(0) # 1. dummy本身初始化的值并无所谓，2. 需要两个变量，因为dummy这个指针不能动，动了就找不到return value了
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2 # 比下面的答案更简洁的写法
        return dummy.next


# 05-12-2022
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 做题时发现的问题：算法很简单，逻辑也很明确，但是细节上不知如何implement
        dummy = ListNode() # 首先需要一个dummy node来初始化整个list
        curr = dummy # dummy本身是不动的，利用一个指针来移动
        
        while l1 and l2: # 使用and而不是or，因为当一方走到头时，另一方后面的部分就不需要再进行对比了
            if l1.val <= l2.val:
                # dummy.next = l1
                # curr = l1
                curr.next = l1 # 两个指针，一个将答案list连接到node上，一个在当前node所在list上向后步进
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next # 别忘了让curr这个指针也步进一步
        
        # 最后剩余部分也连到答案list上
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return dummy.next