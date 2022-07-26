# 读题感想：寻找从当前num出发可能获得的最大数字，并不是寻找二者的差值，所以当前num的大小并不重要
# 选2个digit进行交换的组合一共有：n*(n-1)/2种，重点是如何排除肯定不是最优解的组合
# 一些观察：
# 1. 如果num非递增（每一位数字都不小于后面所有的数字），则它已经是最大
# 2. 从左侧开始逐位往后，寻找当前数字后面的最大数字，将二者交换
# 3. 还要考虑的一个case：如果当前数字后面有多个最大数字，和最后一个交换

# 暴力解：n^2
class Solution:
    def maximumSwap(self, num: int) -> int:
        digit = [int(x) for x in str(num)] # map(int, str(num))返回的是一个iterator，不是list
        
        # 从第一位一直走到倒数第二位
        for i in range(len(digit)-1):
            cur = digit[i]
            # 找到它后面最大的数字
            behind = cur
            behind_index = i
            for j in range(i+1, len(digit)):
                if digit[j] >= behind:
                    behind = digit[j]
                    behind_index = j
            
            if behind > cur:
                digit[i], digit[behind_index] = behind, cur
                total = 0
                for element in digit:
                    total = total * 10 + element
                return total
        
        return num


# 倒序遍历：O(n)
# 找出全局最大值（如果有多个，选择最靠右的那个），并找出它左边小于它的元素中最靠左的那个，互相交换
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        max_idx = len(num) - 1
        xi = yi = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                xi = i
                yi = max_idx
        num[xi], num[yi] = num[yi], num[xi]
        return int(''.join([str(x) for x in num]))