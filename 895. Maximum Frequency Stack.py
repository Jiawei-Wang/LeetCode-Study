# 和stack相同支持初始化，以及push，但pop的不是顶层元素，而是最高频的元素，如果有多个最高频，则pop最靠近顶层的那个

# 思考：可以使用一个dict来保留所有元素的频率和出现的index
class FreqStack:

    def __init__(self):
        self.stack = []
        self.dict = dict()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val not in self.dict:
            self.dict[val] = [0, deque([len(self.stack)-1])]
        else:
            self.dict[val][0] += 1
            self.dict[val][1].appendleft(len(self.stack)-1)
        

    def pop(self) -> int:
        if not self.stack:
            return None
        mostFreqKey = max(self.dict, key=self.dict.get) # get the biggest freq, if multiple elements have same freq return the one with highest index
        self.dict[mostFreqKey][0] -= 1
        index = self.dict[mostFreqKey][1].popleft()
        return self.stack[index] # 如果stack.pop(index)的话会导致其他元素位置发生变动，dict中的index表就失效了，所以直接让元素留在原地
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


"""
Hash map freq will count the frequence of elements.
Hash map m is a map of stack.
If element x has n frequence, we will push x n times in m[1], m[2] .. m[n]
maxfreq records the maximum frequence.

push(x) will push x to m[++freq[x]]
pop() will pop from m[maxfreq]
"""
class FreqStack:
    def __init__(self):
        self.freq = collections.Counter()
        self.m = collections.defaultdict(list)
        self.maxf = 0

    def push(self, x):
        freq, m = self.freq, self.m
        freq[x] += 1
        self.maxf = max(self.maxf, freq[x])
        m[freq[x]].append(x)

    def pop(self):
        freq, m, maxf = self.freq, self.m, self.maxf
        x = m[maxf].pop()
        if not m[maxf]: self.maxf = maxf - 1
        freq[x] -= 1
        return x
    
    
    """
    理解：
    freq中记录所有元素和它们的频率
    m是一个dict，每个元素是一个list，key = freq, value = 此freq中出现的所有元素（先push的排在前面）
    maxf记录当前最大频率
    
    push时更新freq，maxf，然后在m中key=freq的list中添加元素
    pop时先把最大频率的最后一个元素pop出来，然后更新maxf，最后更新freq dict
    """