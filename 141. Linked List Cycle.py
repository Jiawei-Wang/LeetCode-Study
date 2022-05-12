# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # node == node比较的是元素本身而不是元素的值，举例：
        # [1,1,1,1,1]
        # walker = head
        # runner = head.next
        # return walker == runner # False
        
        walker = head
        runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False