# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 将linked list每k个元素进行翻转，最后不足k个的部分保持原位
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        
        # find the k+1 node
        while curr and count != k:
            curr = curr.next
            count += 1
        
        # if k+1 node is found
        if count == k:
            curr = self.reverseKGroup(curr, k) # reverse list with k+1 node as head
            # head - head-pointer to direct part, 
            # curr - head-pointer to reversed part;
            while count > 0: # reverse current k-group
                count -= 1
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
            head = curr
        return head