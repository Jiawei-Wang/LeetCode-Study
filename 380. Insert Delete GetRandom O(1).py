# if we use a set: insert and remove are O(1), however there is no index for getRandom
# if we use something with index: insert and remove will no longer be O(1)
# solution: use two data structures
# a list to store element
# a hashmap to store element's index in list
import random
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {} 
    
    # insert is easy, just append element to list and write down index in hashmap
    # O(1)
    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    # remove is harder, because we are working on a list, remove is usually O(n)
    # solution: use tail to overwrite cur, pop old tail from list, remove cur from hashmap
    # O(1)
    def remove(self, val: int) -> bool:
        if val in self.pos:
            # for cur and tail
            # we know value of cur, index of tail
            # we don't know index of cur, value of tail
            # so first get these two 
            cur_idx = self.pos[val]
            last_element = self.nums[-1]

            # cur has val and cur_idx
            # tail has last_element and -1

            # then we use tail to overwrite cur
            self.nums[cur_idx] = last_element
            self.pos[last_element] = cur_idx

            # lastly remove old tail from list and remove cur from hashmap
            self.nums.pop()
            self.pos.pop(val, 0) # dict.pop(key, 0): (deletes the key, returns its value) or (returns 0)
            
            return True
        return False

    # getRandom is easy, just pick random one from list
    # O(1)
    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()