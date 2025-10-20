# thinking process: 
# using one hashmap (key: word, value: frequency) will allow O(1) inc and dec
# but getMaxKey and getMinKey are impossible
# so we need another data structure to find word using frequency
# doubly linked list + hashmap
# double linked list: each node stores frequency + words of this frequency
# hashmap: key is the word, value is the double linked list node

# first design the node class
class Block:
    def __init__(self, val=0):
        self.val = val # frequency
        self.keys = set() # keys: all the words with this frequency
        self.before = None
        self.after = None

    # method to remove current node
    def remove(self):
        self.before.after = self.after
        self.after.before = self.before
        self.before, self.after = None, None

    # method to insert new node after current node
    def insert_after(self, new_block):
        old_after = self.after
        self.after = new_block
        new_block.before = self
        new_block.after = old_after
        old_after.before = new_block

# then use the node class and hashmap to build main class
class AllOne:
    def __init__(self):
        self.begin = Block()
        self.end = Block()
        self.begin.after = self.end
        self.end.before = self.begin
        self.mapping = {} # hashmap
        
    def inc(self, key: str) -> None:
        # find where this string currently is
        if key not in self.mapping: 
            current_block = self.begin
        else:
            current_block = self.mapping[key]
            current_block.keys.remove(key)

        # check where it should be after incrementing
        if current_block.val + 1 != current_block.after.val:
            new_block = Block(current_block.val + 1)
            current_block.insert_after(new_block)
        else:
            new_block = current_block.after

        # update the node information and hashmap information
        new_block.keys.add(key)
        self.mapping[key] = new_block

        # remove empty node
        if not current_block.keys and current_block.val != 0:
            current_block.remove()
        
    def dec(self, key: str) -> None:
        if not key in self.mapping:
            return

        # find the node
        current_block = self.mapping[key]
        
        # update the node information and hashmap information
        # (currently it's just deletion)
        del self.mapping[key] 
        current_block.keys.remove(key)

        # if freq is not 1, which means after dec it is not 0
        # we need to add the information back
        if current_block.val != 1:
            # check where it should be after decrementing
            if current_block.val - 1 != current_block.before.val:
                new_block = Block(current_block.val - 1)
                current_block.before.insert_after(new_block)
            else:
                new_block = current_block.before
            # add the information back
            new_block.keys.add(key)
            self.mapping[key] = new_block

        # delete current block
        if not current_block.keys:  
            current_block.remove()
        
    def getMaxKey(self) -> str:
        # if no word exists
        if self.end.before.val == 0:
            return ""
        
        key = self.end.before.keys.pop()  # pop and add back to get arbitrary (but not random) element
        self.end.before.keys.add(key)
        return key
        
    def getMinKey(self) -> str:
        # same logic as getMaxKey
        if self.begin.after.val == 0:
            return ""
        key = self.begin.after.keys.pop()
        self.begin.after.keys.add(key)
        return key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()