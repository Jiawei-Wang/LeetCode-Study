# only keep one element in one queue and put the rest in another queue
class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()
        self.single = 0 # indicate which queue has only 1 element

    def empty(self) -> bool:
        return not self.first and not self.second

    def push(self, x: int) -> None:
        if self.empty(): # if there is nothing, push to first queue
            self.first.append(x)
            self.single = 1 # now first queue has 1 element, second has none
        else: 
            if self.single == 1: # we have 1 element in first, all rest (can be any number: 0, 3, anything) in second
                self.second.append(self.first.popleft()) # we move this one to second
                self.first.append(x) # and append new one to first
            else:
                self.first.append(self.second.popleft())
                self.second.append(x)
        
    def pop(self) -> int:
        if self.empty():
            return None
        else:
            if self.single == 1:
                value = self.first.popleft() 
                # now first is empty, we move everything from second to first, leave one in second
                for i in range(len(self.second)-1): 
                    self.first.append(self.second.popleft())
                self.single = 2
                # corner case: one in first, none in second, we pop from first, and mark second as self.single
                # but actually both 2 queues are empty
                # so for any other operations, we still need to do self.empty() check first 
                # rather than using the self.single indicator directly
                return value
            else:
                value = self.second.popleft()
                for i in range(len(self.first)-1):
                    self.second.append(self.first.popleft())
                self.single = 1
                return value

    def top(self) -> int:
        if self.empty():
            return None
        else:
            if self.single == 1:
                return self.first[0]
            else:
                return self.second[0]

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()