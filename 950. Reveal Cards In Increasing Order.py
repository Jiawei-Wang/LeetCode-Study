class Solution1:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 解法1：找出reveal的顺序然后将元素依次填入
        
        # 有三种可选的数据结构：
        # 使用list来实现queue:
        """
        List is a Python’s built-in data structure that can be used as a queue. Instead of enqueue() and dequeue(), append() and pop() function is used. 
        However, lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all of the other elements by one, requiring O(n) time.
        
        use list as queue:
        list = [10,20,30]
        print(list) 
        list.insert(0,5) # add from head
        print(list) # [5, 10, 20, 30]
        list.append(40) # add from tail
        print(list) # [5, 10, 20, 30, 40]
        list.pop(0) # remove from head
        print(list) # [10, 20, 30, 40]
        list.pop(-1) # remove from tail
        print(list) # [10, 20, 30]
        """
        
        # 使用collections.deque
        """
        use deque: Doubly Ended Queue
        append and pop from both ends are O(1)

        # append(): insert the value in its argument to the right end of the deque.
        # appendleft(): insert the value in its argument to the left end of the deque.
        # pop(): delete an argument from the right end of the deque.
        # popleft(): delete an argument from the left end of the deque. 

        from collections import deque
        queue = deque([10, 20, 30])
        print(queue) # deque([10, 20, 30])
        queue.append(40) # add to tail
        queue.appendleft(5) # add to head
        print(queue) # deque([5, 10, 20, 30, 40])
        queue.pop() # pop tail
        queue.popleft() # pop head
        """
        
        # 使用queue.Queue
        """
        use queue.Queue

        # get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
        # put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.

        from queue import Queue
        q = Queue(maxsize = 0) # 0 means infinite size
        q.put(10)
        print(q) # <queue.Queue object at 0x7fe788366d90>
        print(q.get()) # 10
        """
        
        N = len(deck)
        index = collections.deque(range(N)) # deque([0, 1, 2, ..., N-1])
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans

        # Time complexity:
        # O(NlogN) to sort,
        # O(N) to construct using deque or queue.