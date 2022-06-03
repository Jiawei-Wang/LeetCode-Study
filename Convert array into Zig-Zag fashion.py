# time n space 1
class Solution:
	def zigZag(self, arr, n):
    # Flag true indicates relation "<" is expected,
    # else ">" is expected. The first expected relation is "<"
        flag = True
        for i in range(n-1):
            # "<" relation expected
            if flag is True:
                # If we have a situation like A > B > C,
                # we get A > C < B
                # by swapping B and C
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                # ">" relation expected
            else:
                # If we have a situation like A < B < C,
                # we get A < C > B
                # by swapping B and C    
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = bool(1 - flag)
        return arr


# 解法2：因为index为奇数的数字总是大于左右两边index为偶数的数字，所以直接对奇数数字进行检查，如果不满足则翻转即可