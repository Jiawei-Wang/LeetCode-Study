# 读题感想：寻找当前num选2个digit进行交换可能获得的最大数字
# 并不是寻找二者的差值，所以当前num的大小并不重要
# 选2个digit进行交换的组合一共有：n*(n-1)/2种，重点是如何排除肯定不是最优解的组合
# 一些观察：
# 1. 如果num非递增（每一位数字都不小于后面所有的数字），则它已经是最大
# for example: 43321, no swap needed
# 2. 从左侧开始逐位往后，寻找当前数字后面的最大数字，将二者交换
# for example: 21113, swap 2 and 3
# 2-1. not all swap should happen with first digit 
#      if first digit is the largest, then nothing happens to it
# for example: 41332, 4 should not move, swap 1 and 3
# 2-2. 还要考虑的一个case：如果当前数字后面有多个最大数字，和最后一个交换
# for example: 41332, swap 1 and last 3


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
                if digit[j] >= behind: # if multiple, choose the last one
                    behind = digit[j]
                    behind_index = j
            
            # swap
            if behind > cur:
                digit[i], digit[behind_index] = behind, cur
                total = 0
                for element in digit:
                    total = total * 10 + element
                return total
        
        return num
    
    # examples:
    # 43321: nothing happens
    # 21113: when at 2, 3 is found, swap happens
    # 41332: when at 4, nothing happens
    #        when at 1, last 3 is found, swap happens


# 倒序遍历：O(n)
# 找出全局最大值（如果有多个，选择最靠右的那个），并找出它左边小于它的元素中最靠左的那个，互相交换
# examples:
# 43321: nothing happens
# 21113: when at 3, 2 is found, swap happens 
# 41332: when at 2, 1 is found
#        when at last 3, 1 is found, swap happens
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        max_idx = len(num) - 1
        xi = yi = 0
        for i in range(len(num) - 1, -1, -1):
            # if new global maximum is found
            if num[i] > num[max_idx]: 
                max_idx = i

            # we don't need global maximum on the left side
            # if num[i] == num[max_idx]: do nothing
            
            # if smaller element on left side of global maximum is found
            # this smaller element is the current left most one
            # so we don't need to compare it to other smaller ones
            elif num[i] < num[max_idx]:
                xi = i
                yi = max_idx
        
        num[xi], num[yi] = num[yi], num[xi]
        return int(''.join([str(x) for x in num]))