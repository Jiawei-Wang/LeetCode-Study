# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # use a stack for dfs 
        # for an element in the stack: [nestedList, index]
        # it means: I am currently iterating nestedList, and I’m at position index
        self.stack = [[nestedList, 0]] # so we start with top level list and index 0 
        
    
    def next(self) -> int:
        self.hasNext() # this call ensures stack top is positioned at an integer
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
    

    def hasNext(self) -> bool:
        s = self.stack
        while s:
            nestedList, i = s[-1] # get current nestedList
            if i == len(nestedList): # if we have iterated over the whole nestedList
                s.pop() # go back one level in dfs
            else:
                x = nestedList[i] # get current element
                if x.isInteger():
                    return True
                # if x is not an integer
                s[-1][1] += 1 # advance the index
                s.append([x.getList(), 0]) # put child nestedList into stack
        
        # if stack is empty
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())