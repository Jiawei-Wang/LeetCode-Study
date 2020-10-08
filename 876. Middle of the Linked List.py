# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 读题第一想法：使用两个pointer，一个每次走一步，另一个走两步，第二个走到头就返回第一个
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        """
        if fast == None or fast.next == None:
            return slow
        else:
            slow = slow.next
            fast = fast.next.next

        为什么上面的代码返回为空集
        """
