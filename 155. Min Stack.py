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
