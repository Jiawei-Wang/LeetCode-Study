# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        stack = [] # Save <index, value> pair to the stack
        while head:
            while stack and stack[-1][1] < head.val:
                answer[stack.pop()[0]] = head.val
            stack.append([len(answer), head.val]) # len(answer) is the 'index' of the current node 
            answer.append(0)
            head = head.next
        return answer

"""
1. go over linked list once
2. move one node forward:
    1) check how many nodes before it can be updated in answer, pop then out from stack and update them in answer
    2) put current node index and value into stack and give default 0 into answer
3. move one node forward
"""
        