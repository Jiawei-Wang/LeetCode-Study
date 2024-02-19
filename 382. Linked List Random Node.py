# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.all = []
        while head:
            self.all.append(head.val)
            head = head.next
        self.length = len(self.all)

    def getRandom(self) -> int:
        index = random.randint(0, self.length-1)
        return self.all[index]
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# reservoir sampling problem with k = 1
import random
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        res, n = 0, 0  # res: reservoir, n: counter
        h = self.head
        while h:
            n += 1
            if random.randint(1, n) == 1:  # randint(a, b) draws from [a, b], so it has a probability of 1/n to be 1.
                res = h.val  # If it equals 1, it is chosen and should replace the reservoir
            h = h.next
        return res