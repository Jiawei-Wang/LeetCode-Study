# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# one liner: just use an array
class FrontMiddleBackQueue(object):

    def __init__(self):
        self.A = []

    def pushFront(self, val):
        self.A.insert(0, val)

    def pushMiddle(self, val):
        self.A.insert(len(self.A) / 2, val)

    def pushBack(self, val):
        self.A.append(val)

    def popFront(self):
        return (self.A or [-1]).pop(0)

    def popMiddle(self):
        return (self.A or [-1]).pop((len(self.A) - 1) / 2)

    def popBack(self):
        return (self.A or [-1]).pop()
        


# O(1) time solution: two queues
class FrontMiddleBackQueue:

    def __init__(self):
        self.A, self.B = collections.deque(), collections.deque()

    # pushFront and pushBack are easy
    # rebalance the two queues after each operation
    def pushFront(self, val):
        self.A.appendleft(val)
        self.balance()

    def pushBack(self, val):
        self.B.append(val)
        self.balance()

    # popFront and popBack are hard
    # basic idea is to always have len(A) >= len(B)
    # so popFront needs to only check A
    # popBack checks B first, then checks A if there is only one element
    # also reblance after each operation
    def popFront(self):
        val = self.A.popleft() if self.A else -1
        self.balance()
        return val

    def popBack(self):
        val = (self.B or self.A or [-1]).pop()
        self.balance()
        return val

    # for the logic above, we need to keep A.size() >= B.size()
    def balance(self):
        if len(self.A) > len(self.B) + 1:
            self.B.appendleft(self.A.pop())
        if len(self.A) < len(self.B):
            self.A.append(self.B.popleft())

    # pushMiddle and popMiddle are harder
    # since we want to always use A
    # for [1,2,3,4,5,6]:
    #     push: [1,2,3,x,4,5,6]
    #     pop: [1,2,4,5,6]
    # we need A = [1,2,3] and B = [4,5,6]
    # for [1,2,3,4,5]:
    #     push: [1,2,x,3,4,5]: we need A = [1,2] and B = [3,4,5]
    #     pop: [1,2,4,5]: we need A = [1,2, 3] and B = [4,5]

    # so for push middle we need len(A) <= len(B)
    def pushMiddle(self, val):
        if len(self.A) > len(self.B):
            self.B.appendleft(self.A.pop())
        self.A.append(val) # this will result in len(A) == len(B) or len(A) == len(B) + 1, no rebalance needed

    # for pop middle we need len(A) >= len(B)
    def popMiddle(self):
        val = (self.A or [-1]).pop()
        self.balance()
        return val



    