# 和stack相同支持初始化，以及push，但pop的不是顶层元素，而是最高频的元素，如果有多个最高频，则pop最靠近顶层的那个

# 思考：可以使用一个dict来保留所有元素的频率和出现的index
class FreqStack:

    def __init__(self):
        self.stack = []
        self.dict = dict()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val not in self.dict:
            self.dict[val] = [1, deque([len(self.stack)-1])]
            # this val appears 1 (once), and it's at index = len(self.stack)-1 in stack
        else:
            self.dict[val][0] += 1
            self.dict[val][1].appendleft(len(self.stack)-1)
            # this val appears 1 more time, and its latest one is at index = len(self.stack)-1
        

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



class FreqStack:
    def __init__(self):
        # key: element, value: frequency
        # for example: {3:5}: value 3 exists 5 times 
        self.freq = collections.Counter()  

        # key: frequency, value: list of elements with this frequency
        # for example: {6: [2, 3]}: value 2 exists 6 times, value 3 also exists 6 times
        self.m = collections.defaultdict(list) 

        # int to keep track of maximum frequency
        self.maxf = 0 

    def push(self, x):
        self.freq[x] += 1 # for example {3:5} -> {3:6}
        self.maxf = max(self.maxf, self.freq[x]) # check if we need to update maximum frequency
        self.m[self.freq[x]].append(x) # {6: [2, 3]} lastest element will be added to the end of list

    def pop(self):
        x = self.m[self.maxf].pop() # pop the lastest element with the maximum frequency
        self.freq[x] -= 1 
        if not self.m[self.maxf]: 
            self.maxf -= 1
        return x

    """
    for example push 2, 3, 3, 2
    each step we have 
        1) freq {2: 1}
           m    {1: [2]}
        2) freq {2:1, 3:1}
           m    (1: [2,3])
        3) freq {2:1, 3:2}
           m    {1: [2,3], 2: [3]}
        4) freq {2:2, 3:2}
           m    {1: [2,3], 2: [3,2]}
    so we pop 2, then pop 3, then pop 3, then pop 2
    """
    
    
