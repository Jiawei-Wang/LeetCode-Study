# 考察点：如何从set中O(1) 随机取出一个元素，如果使用别的数据结构的话，insert和remove就不是O(1)

import random
class RandomizedSet:
    # 使用一个list来存储被用来随机读取的元素，然后用一个dict来存储它们的位置信息
    def __init__(self):
        self.nums = []
        self.pos = {}
    
    # 先检查元素是否存在，如果否，则插入队尾，并更新dict
    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    # 从dict中找到这个元素的位置，用队尾元素和其对换，然后删除队尾元素，同时更新dict
    def remove(self, val: int) -> bool:
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    # 使用remove()来维持数据结构，所以getRandom()只需要从list中随机返回一个即可
    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()