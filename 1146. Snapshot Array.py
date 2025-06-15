# brute force
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_counter = -1

        self.hashmap = defaultdict(list)
        for key in range(length):
            self.hashmap[key].append(0)

    def set(self, index: int, val: int) -> None:
        self.hashmap[index][-1] = val
        

    def snap(self) -> int:
        for key in self.hashmap:
            self.hashmap[key].append(self.hashmap[key][-1])
        self.snap_counter += 1
        return self.snap_counter

    def get(self, index: int, snap_id: int) -> int:
        return self.hashmap[index][snap_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)