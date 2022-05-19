class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1 (because the result is s[i,j], so j needs to be at least 1)
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                if end == 0 or j-i < end-start:  #find a new current best answer
                    start, end = i, j
                need[s[i]] += 1                  #move i to next element in s
                missing += 1                     
                i += 1                           
        return s[start:end]
    
    
    """
    对于答案的理解：
    1. 遍历每个元素，一开始substring未达到'包含所有t中元素'的条件，所以会在第一个if statement中循环
    2. 第一次刚进入第二个if statement时：此时s[i,j]是从0开始一直到j为止的符合条件的第一个substring（大概率不是最优解）
    3. 此时如果从左侧可以删掉多余元素，则进入while循环一直删
    4. 如果已经没有可以继续删的，则让左指针步进一步，进入下个循环
    
    例子：
    s = 'DABDCAB', t = 'ABC'
    我们知道最佳答案是末尾的'CAB'
    程序执行顺序：
    1. 首先会从[0,0]一直搜到[0,5]，此时substring是'DABDC'，满足包含所有t中元素的条件，进入第二个if statement
    2. 因为最左边的'D'多余，所以删减至'ABDC'，记录此时答案[1,5]
    3. i, j同时步进，检查[2,6]，符合条件，查看是否可以删减，并不能，因为长度与[1,5]相同，所以不被记录
    4. i, j同时步进，检查[3,7]，符合条件，查看是否可以删减，减去3，得到[4,7]，记录此答案
    5. 完成for循环，输出[4,7]
    """