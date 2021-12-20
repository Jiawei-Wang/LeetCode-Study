class Solution:
    def minSteps(self, n: int) -> int:
        """
        因为剪切板中的内容只会以2的阶乘为倍数变长，不会缩短，所以目标数字可分为三种：
        1. 不能被2或者3整除：只能一个一个复制粘贴
        2. 能被2整除：将问题变成子问题：minSteps（n/2）
        3. 能被3整除：将问题变成子问题：minSteps（n/3）
        """
        if n == 1:
            return 0
        if n == 2:
            return 2
        if n == 3:
            return 3
        
        if n % 2 and n % 3:
            return n
        elif not n % 2:
            return self.minSteps(n//2) + 2
        elif not n % 3:
            return self.minSteps(n//3) + 3
        """
        以上答案是错误的，比如
        Input：25
        Output: 10
        因为我们可以使用5个5来获得
        """