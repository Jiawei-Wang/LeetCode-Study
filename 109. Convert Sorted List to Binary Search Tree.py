# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# find the middle one in each recursion
# n to find middle node
# log n to build tree
# nlogn
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.toBST(head, None)

    def toBST(self, head: ListNode, tail: ListNode) -> TreeNode:
        if head == tail:
            return None

        slow = head
        fast = head

        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.val)
        root.left = self.toBST(head, slow)
        root.right = self.toBST(slow.next, tail)

        return root
    

# turn linked list to array first then build tree
# n
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Step 1: Convert linked list to array
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        # Step 2: Build BST from array
        def buildBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)
            return node

        return buildBST(0, len(nums) - 1)
