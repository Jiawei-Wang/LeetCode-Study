class MinStack:

    def __init__(self):
        self.q = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));

    def pop(self):
        self.q.pop()

    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]

'''
学习implement一个stack：

init：创建一个空list

push：在push的同时把当前的min也放进去

pop：正常pop末尾元素

top：返回末尾元素的第一个

getMin：返回末尾元素的第二个

'''



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# 05-11-2022
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
1.理解题意：设计一个stack，可以push，pop，top，getMin
2.example
3.corner cases
4.DSA: element + cur_min
"""
class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append((x, min(self.getMin(), x))) 
           
    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return float('inf')   


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
2024
linked list as stack
"""
class ListNode:
    def __init__(self, val, min, next = None):
        self.val = val
        self.min = min
        self.next = next

class MinStack:
    def __init__(self): # create a dummy node and assign to pointer
        self.current = None

    def push(self, val: int) -> None: 
        # first get the node.min from top node
        if self.current == None:
            getMin = float("inf") # dummy doesn't have node.min
        else:
            getMin = self.getMin()
        # second create a new node and update pointer
        currentMin = min(getMin, val)
        node = ListNode(val, currentMin, self.current)
        self.current = node 

    def pop(self) -> None:
        pop = self.current
        self.current = self.current.next

    def top(self) -> int:
        top = self.current.val
        return top

    def getMin(self) -> int:
        getMin = self.current.min
        return getMin

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()