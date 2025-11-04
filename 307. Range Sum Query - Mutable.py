class NumArray:
    # O(1)
    def __init__(self, nums: List[int]):
        self.nums = nums

    # O(1)
    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    # O(n)
    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


class NumArray:
    # O(n)
    def __init__(self, nums: List[int]):
        self.nums = []
        self.total = []
        total = 0
        for num in nums:
            self.nums.append(num)
            total += num
            self.total.append(total)
        self.length = len(self.nums)

    # O(n)
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        for i in range(index, self.length):
            self.total[i] += diff
        self.nums[index] = val

    # O(1)
    def sumRange(self, left: int, right: int) -> int:
        return self.total[right] - self.total[left-1] if left >= 1 else self.total[right]  


"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval. All of the leaves will store
    elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

#Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #helper function to create the tree from input array
        def createTree(nums, l, r):
            
            #base case
            if l > r:
                return None
                
            #leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            
            root = Node(l, r)
            
            #recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            
            #Total stores the sum of all leaves under root
            #i.e. those elements lying between (start, end)
            root.total = root.left.total + root.right.total
                
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateVal(root, i, val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)
            
            #Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total
            
            return root.total
        
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def rangeSum(root, i, j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, i, j)


# 2025
"""
Prefix Sum
1. build: O(n)
2. query: O(1)
3. update: O(n)
space: O(n)

Segment Tree:
1. build: O(n)
2. query: O(logn)
3. update: O(logn)
space: O(4 * n) still linear
"""
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start # start index of this segment
        self.end = end # end index of this segment
        self.sum = 0 # sum of this segment
        self.left = None # left child 
        self.right = None # right child

"""
For example:
["NumArray",  "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2],     [1, 2],   [0, 2]]

After each call:

1. build tree
               [0,2] sum=9
              /             \
        [0,1] sum=4       [2,2] sum=5
        /         \
[0,0] sum=1   [1,1] sum=3

2. sumRang(0, 2)
no change, just query and return

3. update(1, 2)
               [0,2] sum=8
              /             \
        [0,1] sum=3       [2,2] sum=5
        /         \
[0,0] sum=1   [1,1] sum=2

4. sumRange(0, 2)
no change, just query and return
"""

class NumArray:

    def __init__(self, nums: List[int]):
        # Build the segment tree
        def buildTree(l, r):
            if l > r:
                return None
            node = SegmentTreeNode(l, r)
            if l == r:
                node.sum = nums[l]
            else:
                mid = (l + r) // 2
                node.left = buildTree(l, mid)
                node.right = buildTree(mid + 1, r)
                node.sum = node.left.sum + node.right.sum
            return node

        if nums:
            self.root = buildTree(0, len(nums) - 1)
        else:
            self.root = None

    def update(self, index: int, val: int) -> None:
        # Update a value in the segment tree
        def updateTree(node, i, val):
            if node.start == node.end == i:
                node.sum = val
                return
            mid = (node.start + node.end) // 2
            if i <= mid:
                updateTree(node.left, i, val)
            else:
                updateTree(node.right, i, val)
            node.sum = node.left.sum + node.right.sum
        
        if self.root:
            updateTree(self.root, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        # Query a range sum in the segment tree
        def rangeSum(node, l, r):
            # The query range [l, r] fully matches the node’s range
            if node.start == l and node.end == r:
                return node.sum
            mid = (node.start + node.end) // 2
            # The query range is completely inside the left or right child
            if r <= mid: 
                return rangeSum(node.left, l, r)
            elif l > mid:
                return rangeSum(node.right, l, r)
            # The query overlaps both left and right
            else: 
                return rangeSum(node.left, l, mid) + rangeSum(node.right, mid + 1, r)
        
        return rangeSum(self.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)