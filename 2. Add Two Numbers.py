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


# 2024
# modify l1 in place
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        head1 = l1
        head2 = l2
        carry = 0
        while head1 and head2:
            head1.val += carry + head2.val 
            carry = head1.val // 10
            head1.val = head1.val % 10
            tmp = head1
            head1 = head1.next # in case head1 is None, we can use tmp to get last head1 
            head2 = head2.next
        
        if not head1 and not head2: # if both linked lists are of same length
            if carry:
                tmp.next = ListNode(1)
        elif not head2: # if l1 is longer, keep updating head1
            while head1:
                head1.val += carry
                carry = head1.val // 10
                head1.val = head1.val % 10
                tmp2 = head1
                head1 = head1.next # in case head1 is None, we can use tmp2 to get last head1
            if carry:
                tmp2.next = ListNode(1)
        else: # if l2 is longer, connect head1 to head2, then modify head2
            tmp.next = head2 # tmp is the last head1
            while head2:
                head2.val += carry
                carry = head2.val // 10
                head2.val = head2.val % 10
                tmp3 = head2 # in case head2 is None, we can use tmp3 to get last head2
                head2 = head2.next
            if carry:
                tmp3.next = ListNode(1)

        return l1


