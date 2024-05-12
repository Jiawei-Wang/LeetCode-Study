# in a square matrix with length >= 1, find the k-th smallest element (not k-th distinct element)
# matrix is sorted on each row and each col 
# it doesn't mean: matrix is strictly non-decreasing row by row
# for example: 
#    1    5    9
#    10   11   13
#    12   13   15
# notice 12 on third row is smaller than 13 on second row
# and if k = 8, we should return 13 as 13 is the second in [1,5,9,10,11,12,13,13,15], and 8-th overall


# solution 1:
# max heap: only keep k smallest elements and pop anything larger
# this solution doesn't use the given information: matrix is sorted 
# time: M * N * logK
# space: K
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])  # For more general questions where matrix is not always a square
        maxHeap = []
        for r in range(row):
            for c in range(col):
                heapq.heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        return -heappop(maxHeap)


# solution 2:
# rows are sorted, so question becomes: finding k-th smallest element among all M sorted rows
# similar to merge M sorted linked lists
# so we use a min heap and a pointer on each row 
# time K * log K
# space K
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square
        minHeap = []  # val, r, c

        # first put all first element of all rows into min heap
        # if k<m: 
        #    we want to find 4-th smallest element and we have 6 rows
        #    since cols are sorted, so first col alone will guarantee:
        #    answer value <= first element on 4-th row
        #    so in this case we just need first k rows 
        for r in range(min(k, m)):
            heappush(minHeap, (matrix[r][0], r, 0))
        
        # then we keep popping k times 
        # there are min(k, m) elements in min heap already so we will get empty heap
        # but we still need to add element into heap because:
        # if [3, 2] is the current smallest one in heap
        # we know nothing about [4, 2] and [3, 3]
        for i in range(k): 
            ans, r, c = heappop(minHeap) 
            if c + 1 < n: 
                heappush(minHeap, (matrix[r][c + 1], r, c + 1)) 

        # last pop is the k-th smallest         
        return ans   


# solution 3: 
"""
Algorithm: Binary search
Time: (M+N) * logD (D is biggest element - smallest element)
M+N: check method
logD: search loop
Space: 1

Previous solutions don't utilize all information so they are not optimal:
1. more information can be derived from (rows and cols are sorted):
    1) we know [0, 0] is the smallest, [-1, -1] is the biggest
        1> so the search range D is known
        2> so it is possbile to pick a number within range and check if it is a good number
        3> so the most efficient way is binary search 
    2) to implement binary search, we use mid = x = (low + high)//2 in each range
        1> imagine using x to divide matrix into 4 parts: topleft, topright, bottomleft, bottomright
            1- the element on topleft side (including current row and current col) of x is guaranteed to be <= x
               the element on topleft side (not including current row and current col) of x is guaranteed to be < x
            2- the element on bottomright side (including current row and current col) of x is guranteed to be >= x
               the element on bottomright side (not including current row and current col) of x is guaranteed to be > x
            (example: everything on the same row and same col as x are also x)
            3- we don't know about topright and bottomleft
2. now we know we want to use binary search and we have a mid for each loop, we need a check method for the chosen mid = x:
    1) our goal is to find the k-th smallest element
        1> so the method should check how many elements in matrix <= x
        2> so brute force way is to check all elements (m*n)
        3> but from 1.2.1.2 the information regarding bottomright side, we know: 
           if y > x: everything between (y's location) and [-1, -1] are > x 
           (because everything in this bottomright part >= y, including the same row and col)
        5> because on any row there might be elements smaller than x:
           for example: the whole topleft part + some elements in topright + some elements in bottomleft
           we need to check each row
        6> so for each row, there is a cut off col (see 2.1.3), and the rows below this row don't have to go through this col again
        7> so the check method becomes: 
            1- start from first row to last row
            2- start from last col to first col
            3- find cut off col on each row
3. how to loop using return value of check method:
    1) check(x) returns an int i: number of elements with value <= x
    2) i can be >k, =k, or <k
    3) if <k: we know x is too small 
    4) if =k: we don't know anything:
       x represents mid in a range, it doesn't always exist as an element in matrix
       for example check(5) = k, 5 doesn't exist, 4 exists, and check(4) also = k
       or 6 exists, and check(6) also = k
    5) if >K: we know x is upper bound for the real value
    6) so combined together, we know:
        1> if <k: real value > x
        2> if >=k: real value <= x
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # check method
        def countLessOrEqual(x): # return the number of elements <= x
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: 
                    c -= 1  # decrease column until matrix[r][c] <= x
                cnt += (c + 1) 
            return cnt
        """
        execution:
        1. for first rol, we start from last col, find cut off col, everything on the left is <= x
        2. for second rol, we start from cur off col, find new cut off col, everything on the left is <= x
        3. repeat for all rows
        """

        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square
        left, right = matrix[0][0], matrix[-1][-1] # range of binary search

        while left < right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) < k:
                left = mid + 1
            else:
                right = mid  

        return left