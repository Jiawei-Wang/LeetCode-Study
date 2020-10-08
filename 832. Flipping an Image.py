class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # 遍历每个row
        for i in range(len(A)):
            # 进行翻转: 每两个元素互相交换；然后取反
            for j in range((len(A[0])+1)//2):   # 注意这里使用(length+1)/2来确保遍历半个数组
                # ^1的作用：XOR，如果该数为1，则返回0，若为0，则返回1
                temp = A[i][j]^1
                A[i][j] = A[i][len(A[0])-1-j]^1
                A[i][len(A[0])-1-j] = temp
        # 输出
        return A
