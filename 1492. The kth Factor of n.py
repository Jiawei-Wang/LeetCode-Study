# brute force
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        curr = 0
        for i in range(1, n+1):
            if n % i == 0:
                curr += 1
                if curr == k:
                    return i
        return -1


# improved brute force
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # 直接使用 k 就可以少用一个变量
        # 只需要步进到 n/2，如果此时 k == 1，则下一个 factor 一定是 n 自身
        for i in range(1, n//2+1):
            if n % i == 0: k -= 1
            if k == 0: return i
        if k == 1:
            return n
        else:
            return -1


# n ^ 0.5 复杂度
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor_list = []
        for factor in range(1, int(math.sqrt(n)) + 1):
            if n % factor == 0:
                if factor ** 2 != n:
                    factor_list.append(factor)
                k -= 1
                if k == 0:
                    return factor
        # 循环完后factor_list中存储的是所有 小于 n ^ 0.5 的factor：
        # 例子：16，那么list中是 1，2，没有4
        # 如果把4放进去的话，会造成重复

        # 如果 k 当前的值大于list长度（也就是原本 k 的值大于list长度的两倍），那么一定没有满足条件的数字，输出-1
        # 否则的话，取倒数第 k 个数对应的那个数字即可
        # 重点是学习这个语法：return a if b else c
        return -1 if k > len(factor_list) else n // factor_list[-k]
        
