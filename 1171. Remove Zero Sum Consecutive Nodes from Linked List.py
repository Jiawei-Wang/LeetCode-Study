# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# prefix sum + store it in hashmap
# example:     3, 4, 2, -6, 1, 1, 5,  -6
# prefix sum:  3, 7, 9,  3, 4, 5, 10, 4
# after deletion of duplicated elements: 3, 4 -> [3, 1]
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict() # OrderedDict keeps the order of insertions
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur) # get seen[prefix], if None return cur
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next