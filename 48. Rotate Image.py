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


