"""
heapq.heapify(list): convert list to heap
heapq.heappush(list, number): push number into heap
heapq.heappop(list): pop smallest element
heapq.heappushpop(list, number): push + pop
heapq.heapreplace(list, number): pop + push
"""
from heapq import heapify, heappush, heappop, heappushpop, heapreplace

# 这道题等同于：如何快速在k个数字中找到最小值，并快速插入新数字
# priority queue / heap 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # lists is a list of all heads for all linked lists, we put all heads into heap
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head] 
        """
        为什么使用(head.val, i, head)而非(head.val, head)：
        heapify会对元素进行比较，如果元素是一个tuple则比较其中第一个元素，如果相等则比较第二个，以此类推
        这里head.val会出现相等，heapify会去比较两个ListNode，然后报错
        """

        heapify(heap)
        dummy = ListNode(0)
        curr = dummy

        while heap != []:
            val, i, node = heap[0] # heap[0]是heap中最小的元素
            curr.next = node    
            curr = curr.next

            if not node.next: # 如果其中一个linkedlist所有元素都被遍历完，则正常pop即可 
                heappop(heap) 
            else: # 如果该linkedlist还剩元素，则先pop当前元素，再将下一个加入heap
                heapreplace(heap, (node.next.val, i, node.next)) # recycling tie-breaker i guarantees uniqueness
            
        return dummy.next


# divide and conquer
# 将所有linkedlist两两相连，然后逐层递进
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # corner case: lists is empty
        if not lists:
            return None

        # if >= 3 linked lists: divide into 1 and 2
        # if 2 linked lists: divide into 1 and 1 
        # if 1 linked list: return head of this linkedlist
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])

        # now merge two heads of two linked lists together
        return self.merge(l, r)
    
    # merge two heads from two linked lists together and return one head
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next