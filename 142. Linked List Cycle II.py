# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# slow moves 1 step at a time, fast moves 2
# when fast meets slow, they are both on the circle somewhere
# x: the length of the linked list before start of the circle
# y: distance from start of the circle to where slow and fast meet
# z: length of whole circle
# so 2 * (x + y) - (x + y) = k * z
# so x + y = k * z
# let slow continue to travel from meeting point (x + y)
# and let another pointer travel from head one step at a time
# after x steps, this pointer (x) and slow (x + y + x) = x + k * z will meet 
# and that meeting point is guaranteed to be the start of the circle
# because per definition, x is the length before start of the circle
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # at least 2 nodes needed to form circle
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next          # move slow by 1
            fast = fast.next.next     # move fast by 2
            if slow == fast:          # collision point -> cycle exists
                break
        else:
            # If we exit the loop normally, there is no cycle
            return None

        # Step 2: Find the start of the cycle
        third = head                   
        while third != slow:
            slow = slow.next          
            third = third.next

        # The node where they meet is the start of the cycle
        return slow