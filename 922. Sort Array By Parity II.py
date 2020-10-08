# 解法1：创建一个新的list，把偶数放在偶数位置，奇数放在奇数位置
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = [-1] * len(A)
        even = 0
        odd = 1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                ans[even] = A[i]
                even += 2
            else:
                ans[odd] = A[i]
                odd += 2
        return ans


# 解法2：in place
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = 1
        for even in range(0, len(A), 2):
            if A[even] % 2 != 0:
                while A[odd] % 2 == 1:
                    odd += 2
                A[even], A[odd] = A[odd], A[even]
        return A
