# hashmap + double linkedlist
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # 先在dictionary中找到key value pair，然后将这个pair提出来，放入linkedlist最后面
    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    # 首先判断是否key已存在，如果存在则在linked list中提出来（不放回去，等于是删除）
    # 然后将新的key value pair放入linked list末尾，同时更新dictionary
    # 放入后可能会出现长度超标，所以判断，如果超标则将LRU从linked list中提出来，然后更新dictionary
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
            
    # 将node从它所在位置除去
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # 将node放入末尾
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# 2024
# hashmap + double linkedlist
# hashmap for quick lookup
# linkedlist for updating cache

# first create a linkedlist node class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None # we need both directions
        self.next = None
    
class LRUCache:
    # then initilize LRU data structures
    # hashmap for quick lookup
    # two dummy nodes for linkedlist
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict() 
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # third we need two helper methods
    def _remove(self, node): # remove node from current location in cache
        # we just need to connect prev and next together 
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node): # add node to the end of cache list
        # we need to insert node between last node and dummy tail
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
    def get(self, key: int) -> int:
        # if key is in hashmap: 1. we return the value, and 2. take it out and put it at the end of LRU
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key is already in hashmap, we remove it from cache
        if key in self.dic:
            self._remove(self.dic[key])
        
        # regardless of if key exists, we update hashmap and add to end of LRU
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n

        # because we are adding new items to cache, we need to check capacity
        if len(self.dic) > self.capacity:
            n = self.head.next # remove the oldest from cache
            self._remove(n)
            del self.dic[n.key] # also remove it from hashmap
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)