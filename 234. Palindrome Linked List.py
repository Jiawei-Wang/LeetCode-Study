# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 暴力解：time n space n
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        n = len(l)
        if n % 2:
            return l[0:n//2] == l[n-1:n//2:-1]
        else:
            return l[0:n//2] == l[n-1:n//2-1:-1]


# 走到中间，然后将前半段翻转（龟兔赛跑 + 翻转linked list）
# time n space 1
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev # 只有走到头了才能返回True，如果中途停止就返回False