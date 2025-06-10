# if the key already existed, the original key-value pair will be overridden to the new one
# therefore two things need to be done
# 1. a data structure to store the key-value pair
# 2. if key-value pair exists: change to new value 
class TrieNode:
    def __init__(self):
        self.sum = 0
        self.child = defaultdict(TrieNode)

class MapSum:
    def __init__(self):
        self.root = TrieNode() # create dummy root
        self.map = defaultdict(int) # create key-value pair store
        
    def insert(self, key: str, val: int) -> None:
        diff = val - self.map[key] # new value - old value
        curr = self.root
        for c in key:
            curr = curr.child[c]
            curr.sum += diff
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.child: return 0
            curr = curr.child[c]
        return curr.sum     


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)