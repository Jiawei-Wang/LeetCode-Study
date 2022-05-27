"""
collections.deque: O(1) for append and pop compared to list (O(n))
    1. append(): insert to right end
    2. appendleft(): insert to left end
    3. pop(): delete from right end
    4. popleft(): delete from left end
    5. index(value, i, j): search from i to j, return the first index of the value
    6. insert(i, value): insert value at i
    7. remove(): remove first occurrence of value
    8. count(): count the number of occurrences of value
    9. extend(iterable): add multiple values at the right end
    10. extendleft(iterable): add multiple values at the left end in reversed order, 
                              for example extendleft([1,2,3]) will have [3,2,1] at the beginning of the dequeue
    11. reverse(): reverse the order of elements
    12. rotate(number): rotate the deque by the number, negative number to the left, positive number to the right, 
                        for example rotate(1) will have every element shift to right for 1 block
"""


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# two stacks
# push: 保持s1中存储顺序和queue相反，新元素被放入s1底部而不是顶部
# 具体操作：如果s1为空，直接加入，如果s1不为空，将s1元素挨个pop出来放入s2，s1放入新元素，再将s2中元素pop出来放回s1
# time n, space n
# pop: 直接pop s1即可, time 1 space 1
# empty: 检查s1 size即可，time 1 space 1
# peek: 加入一个指针front，在push和pop时更新顶部元素, time 1 space 1
from collections import deque
class MyQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
        self.front = None

    def push(self, x: int) -> None:
        if not self.s1:
            self.s1.append(x)
            self.front = x
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.s2.append(x)
            while self.s2:
                self.s1.append(self.s2.pop())

    def pop(self) -> int:
        if self.s1:
            catch = self.s1.pop()
            if self.s1:
                self.front = self.s1[-1]
            else:
                self.front = None
            return catch
        else:
            return None
            
    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return not self.s1


# 对上面解的优化
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1


# 同样还是two stack，但是分别使用不同的stack来处理push和pop，push时正常push，pop时才去转移元素进另一个stack，省去每次push都要重新maintain s1的麻烦
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2