# brute force:
# use hashmap to store all keys, each key has its own list of values
# make a copy of every key's latest value when snap is called
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_counter = -1
        self.hashmap = defaultdict(list)
        for key in range(length):
            self.hashmap[key].append(0)

    def set(self, index: int, val: int) -> None:
        self.hashmap[index][-1] = val
    
    # o(n): each element's list gets appended
    def snap(self) -> int:
        for key in self.hashmap:
            self.hashmap[key].append(self.hashmap[key][-1])
        self.snap_counter += 1
        return self.snap_counter

    # o(1): no search needed
    def get(self, index: int, snap_id: int) -> int:
        return self.hashmap[index][snap_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# binary search on snap_id
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [[[-1, 0]] for _ in range(length)] # initial value is 0 with snap_id -1

    def set(self, index: int, val: int) -> None:
        self.data[index].append([self.snap_id, val])

    # o(1)
    # improvement over the brute force solution
    # no physical copy is appended
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    # o(log(n))
    # worse than brute force solution
    # binary search is needed
    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.data[index], [snap_id + 1]) - 1
        return self.data[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)