# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        array = []

        while head:
            array.append(head.val)
            head = head.next
        
        base_two = "".join(str(digit) for digit in array)
        return int(base_two, 2)