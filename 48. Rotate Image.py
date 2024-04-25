class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # 解法1：built in
        A[:] = zip(*A[::-1])
        """
        A[::-1]将2d list上下翻转
        zip()将多个iterable变成一个object
        例子：
        A = [1,2,3]
        B = ['a', 'b', 'c']
        print(list(zip(A,B)))
        [(1, 'a'), (2, 'b'), (3, 'c')]
        """


        # 解法2：将2d list分为四等分，然后遍历所有左上角等分中的元素，和对应的三个元素对调
        n = len(A)
        for i in range(n//2):
            for j in range(n-n//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = A[~j][i], A[~i][~j], A[j][~i], A[i][j]

        # ~a = -a-1


# 2024
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        # if length is 4, a quarter is [0,0] to [1,1] with no center element in matrix
        # if length is 5, a quarter is [0,0] to [1,1] with [2,2] being the center element in matrix
        # if we select [0,0] to [2,2] as a quarter, some elements will be moved more than once
        quarter_length = length//2
        for i in range(quarter_length):
            for j in range(quarter_length):
                one   = matrix[i][j] 
                two   = matrix[j][length-1-i]
                three = matrix[length-1-i][length-1-j]
                four  = matrix[length-1-j][i]
                
                matrix[i][j]                    = four
                matrix[j][length-1-i]           = one
                matrix[length-1-i][length-1-j]  = two
                matrix[length-1-j][i]           = three
        
        # if length is odd: deal with remaining elements in center horizontal line and in center vertical line
        if length % 2: 
            for i in range(quarter_length):
                one     = matrix[i][quarter_length]
                two     = matrix[quarter_length][length-1-i]
                three   = matrix[length-1-i][length-1-quarter_length]
                four    = matrix[length-1-quarter_length][i]

                matrix[i][quarter_length]                    = four
                matrix[quarter_length][length-1-i]           = one
                matrix[length-1-i][length-1-quarter_length]  = two
                matrix[length-1-quarter_length][i]           = three

