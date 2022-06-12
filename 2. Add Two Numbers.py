# Definition for singly-linked list.
# class ListNode:       # python class: https://www.w3schools.com/python/python_classes.asp
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 三个答案：相同逻辑，不同语法
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


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = n = ListNode()
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10) # divmod(num1, num2): 返回值是一个tuple（整除值，余数）
            n.next = ListNode(val)
            n = n.next
        return root.next