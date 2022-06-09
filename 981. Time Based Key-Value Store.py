# 对于一个key，保存多个value以及timestamp
# get(key, timestamp)：返回所有timestamp<=timestamp的value中的最大者，否则空字符串
# 理解题意：主要考察如何设计value-timestamp的数据结构
class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # why no need to sort: "All the timestamps timestamp of set are strictly increasing."
        arr = self.dic[key]
        n = len(arr)
        
        left = 0
        right = n
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid
        
        return "" if right == 0 else arr[right - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)