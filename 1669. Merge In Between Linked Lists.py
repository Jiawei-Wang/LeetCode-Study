# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_head = list2
        while list2.next:
            list2 = list2.next
        list2_tail = list2

        head = list1
        cut1 = cut2 = list1
        while a > 1:
            list1 = list1.next
            a -= 1
            b -= 1

            cut1 = list1
        
        while b > -1:
            list1 = list1.next
            b -= 1
            cut2 = list1
        
        cut1.next = list2_head
        list2_tail.next = cut2


        return head













