"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


"""
flatten one layer at one time
example:
1 - 2 - 3 - 4 - 5 - 6
        |
        7 - 8 - 9 - 10
            |
            11 - 12
go to 3
put 3 and 4 in memory
go into 7
go to 10
link 3 and 7, 10 and 4
so we removed second layer 
1 - 2 - 3 - 7 - 8 - 9 - 10 - 4 - 5 - 6
                |
                11 - 12
then go to 7, then 8, then do the same thing to 11 and 12
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # corner case
        if not head:
            return None
        
        p = head
        while p:
            # case 1: no child, do nothing
            if p.child == None:
                p = p.next
                continue
            
            # case 2: have child, find tail of the child and link to p.next
            temp = p.child
            while temp.next:
                temp = temp.next
            temp.next = p.next
            if p.next:
                p.next.prev = temp
            p.next = p.child
            p.child.prev = p
            p.child = None
        
        return head
            

        