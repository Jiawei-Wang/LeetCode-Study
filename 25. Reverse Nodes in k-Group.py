# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 将linked list每k个元素进行翻转，最后不足k个的部分保持原位
# (node value cannot be changed, only node connections can be changed)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find the first segment
        curr = head
        count = 0
        while curr and count != k:
            curr = curr.next
            count += 1
        # now curr is point at the k+1 node (the starting node for the 2nd segment) 
        # notice: this node can be None, if we only have first segment

        # if we don't have enough nodes for first segment, we do nothing
        # if we have enough nodes for first segment, we flip everything 
        if count == k: 
            # when we flip, we don't want to mess up the connection, so we flip the last segment first
            # then the one before last one, ..., lastly the first segment
            curr = self.reverseKGroup(curr, k) # so now curr is the new curr for the next segment
            
            while count > 0: # reverse current segment
                # when we first enter this while loop: 
                # head: first element in current segment
                # curr: first element in next segment
                # we let head connect to curr
                # then let head become curr and head.next become new head
                # then repeat
                count -= 1
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
            head = curr
            
        return head