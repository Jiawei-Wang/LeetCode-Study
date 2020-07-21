# Definition for singly-linked list.
# class ListNode:       # python class: https://www.w3schools.com/python/python_classes.asp
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode ,c = 0) -> ListNode:
        # 当前这一位的总和
        val = l1.val + l2.val + c
        c = val // 10
        # 创建一个node并赋值
        ret = ListNode(val % 10 )

        if (l1.next != None or l2.next != None or c != 0):
            # 如果其中一方走到头，就创建一个node并赋值为0
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)

            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
