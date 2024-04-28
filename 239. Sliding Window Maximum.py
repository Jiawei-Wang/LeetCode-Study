"""
1. 理解题意：
    1）我们想要找到每个长度为k的substring中的最大值
    2）nums长度为正，其中元素可正可负，substring的长度不大于nums长度
2. 思考过程：
    substring每次往前步进一步，肯定要O(n)，没有什么特别之处
    使用什么样的数据结构来保存当前信息，保证步进后能最快速度更新信息，才是重点
    (一个需要注意的地方：比如当前substring最大值为5，步进后头部的5被pop掉，仍然无法确定新的substring中还剩几个5)
3. 可能解法：
    1）暴力解：对每个substring进行遍历，O(nk) 
    2）priority queue：O(nlogk)
    3) deque: O(n)
    4) dp: o(n)
"""


"""
Priority Queue in python:
1. PQ vs Heap: PQ is abstract data type, it can be implemented in many ways, including using Heap, a data structure
2. PQ vs Queue: Queue is FIFO, PQ is an extension of Queue with elements having priority
3. heapq in python:
    1) it is a min heap 
    2) heapq.heapify(iterable): convert the iterable into a heap
    3) heapq.heappush(heap, element): insert element into heap
    4) heapq.heappop(heap): remove and return smallest element from heap
    5) heapq.heappushpop(heap, element): push element, then pop the min
    6) heapq.heapreplace(heap, element): pop min first, then push element
"""
# Priority Queue
import heapq as h
class Solution:
    def get_next_max(self, heap, start): # heap会一直pop元素直到pop出第一个index >= start的元素后停止
        while True:
            x, idx = h.heappop(heap)
            if idx >= start:
                return x*-1, idx
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # corner case
        if k == 0:
            return []
        
        # initial state
        heap = []
        for i in range(k): # 用第一个substring中的元素和其坐标来初始化heap
            h.heappush(heap, (nums[i]*-1, i)) # 不需要heapify就可以直接用
        
        # travel through string
        result = []
        start, end = 0, k-1
        while end < len(nums):
            x, idx = self.get_next_max(heap, start) 
            result.append(x)
            h.heappush(heap, (x*-1, idx)) 
            start, end = start + 1, end + 1
            if end < len(nums):
                h.heappush(heap, (nums[end]*-1, end))
        return result
    
"""
对于答案的理解：
1. 其他部分都很明确，先初始化一个heap，然后每次步进一步
2. 对于两次heappush:
    第一次：我们获得本substring的最大值后（通过pop获得），并不知道其是否在下一轮新的substring范围内，所以要再放回去
    第二次：将下一轮的新元素push进heap
3. 对于get_next_max:
    每次进入新的循环会更新start作为界限，此时要做的是将前一轮的头部元素pop出去，但是因为heap没有查询功能，
    所以采取一直pop（每次出来的值逐渐减小），直到发现第一个在界限之内的元素为止，这样做同时也可以让我们不需要维持heap的长度为k
    因为pop出去的值肯定不在本轮substring范围内，所以pop出去多少都无所谓
"""


# deque
# syntax: from collections import deque, a = deque([1,2,3])
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque([0]) # deque中装的是元素的下标，初始化为第一个元素
        ans = []
        for i in range (len(nums)): # i是从尾部新加入的元素的下标
            # 每次进入新一轮时，首先将deque中当前元素中超出此轮范围的元素给pop掉
            # 因为元素总是满足在nums里靠前的，在deque中也靠前（尽管可能index不连续），所以只要popleft即可
            while deq and deq[0] <= i - k: 
                deq.popleft()
            # 然后从deque尾部开始把小于新加入元素的元素给pop掉
            while deq and nums[i] >= nums[deq[-1]] :
                deq.pop()
            deq.append(i)
            # 更新完毕后的deque中最大元素则是此轮答案
            ans.append(nums[deq[0]])
            
        return ans[k-1:]
    
"""
对答案的理解：保持一个单调递减deque，其中所有元素都在此轮substring的范围之内，则头部元素必然是此轮的答案
"""


# https://leetcode.com/problems/sliding-window-maximum/discuss/65881/O(n)-solution-in-Java-with-two-simple-pass-in-the-array
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_left = [float('-inf')] * n
        max_right = [float('-inf')] * n
        
        max_left[0] = nums[0]
        max_right[n-1] = nums[-1]
        
        for i in range(1, n):
            max_left[i] = nums[i] if not i % k else max(max_left[i-1], nums[i])
            j = n - i - 1
            max_right[j] = nums[j] if not j % k else max(max_right[j+1], nums[j])
            
        ans = []
        for i in range(n-k+1):
            ans.append(max(max_right[i], max_left[i+k-1]))
            
        return ans

"""
对答案的理解：不理解，需要重新读帖子
"""


# question: return maximum element in each window
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        bigger = deque() # bigger是一个递减queue, with indexes of numbers
        for i, n in enumerate(nums):

            # 将queue尾部开始所有小于该元素的元素都pop出来, 将该元素加入queue尾部
            # any window containing current element will no longer need previous smaller elements
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()
            bigger += [i]

            # we update queue if it's longer than window
            # 如果尾部元素和头部元素在nums中距离超过k, 则pop掉头部元素
            # although the front element is the biggest, it's no longer in current window, we don't need it
            if i - bigger[0] >= k:
                bigger.popleft()

            # 只有当遍历到第k个元素时, 才开始向res中添加元素
            if i + 1 >= k:
                res.append(nums[bigger[0]])

        return res

"""
1. before we visit the k-th element: we add element to queue, discard smaller ones in the front
2. when we start from the k-th element: we pick front element as answer (guaranteed biggest in window)
3. if queue is full, we discard front element since it is not part of the window anymore


nums = [1,3,-1,-3,5,3,6,7], k = 3
1. for 1: put index 0 into bigger: [0] 
2. for 3: pop 0, put 1: [1] (nums[0] = 1 will not be considered anymore)
3. for -1: put 2: [1, 2], first window full, start to append to res: [3] (nums[1] = 3)
4. for -3: put 3: [1, 2, 3], bigger becomes full (not pop yet), second window full, append to res: [3, 3] (nums[1] = 3 is still the biggest)
5. for 5: pop everything, put 4: [4], append to res: [3, 3, 5] (nums[4] = 5 is the only one, because it's the biggest one)
6. for 3: put 5: [4, 5], append to res: [3, 3, 5, 5]
7. for 6: pop everything, put 6: [6], append to res: [3, 3, 5, 5, 6]
8. for 7: pop everything, put 7: [7], append to res: [3, 3, 5, 5, 6, 7] 
""" 