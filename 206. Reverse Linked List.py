# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iteration 
# time n space 1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 四个注意点：
        # 1. 我们需要三个变量来实现两个node的转换
        # 2. 其中一个变量：prev，需要先被初始化
        # 3. 另一个变量：curr，只存在于每次循环中
        # 4. 在将指针（变量）转移node完成后，剩余任务是将两个node连接起来 
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


# recursion
# time n space n
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        对recursion的理解：
        1. 找到一个起始点
        2. 找到循环的位置
        3. 每次循环提供更新后的变量
        """
        def reverse(curr, prev): # 和iteration一样，需要两个变量，其中prev在下方被初始化为none
            if curr is None:
                return prev
            else:
                nxt = curr.next
                curr.next = prev
                return reverse(nxt, curr) # 更新变量，并带入下一层循环

        return reverse(head, None) # 初始化


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None # need a dummy node first
        current = head 
        while current:
            temp = current.next # need to store next node 
            current.next = previous # change direction
            previous = current # one step forward
            current = temp 

        return previous # at last node, current will point to None and previous to current so we return previous
        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # no need to do anything if there are less than 2 nodes
        if not head or not head.next:
            return head

        prev = None # after reversing, head.next is None, tail.next is no longer None but the second last node
        curr = head

        while curr:
            temp = curr.next # use temp to hold node before breaking the link
            curr.next = prev # break current link
            prev = curr # one step forward
            curr = temp # one step forward
            
        return prev 