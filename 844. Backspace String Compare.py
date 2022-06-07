class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #读题第一想法：两个list，考虑到一个corner case：如果backspace多于现有字符（list为空），则不做改变
        s_list = []
        t_list = []

        for i in S:
            if i != "#":
                s_list.append(i)
            else:
                if s_list:
                    s_list.pop()

        for i in T:
            if i != "#":
                t_list.append(i)
            else:
                if t_list:
                    t_list.pop()

        return s_list == t_list


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        for i in s:
            if i == '#':
                if not s1:
                    continue
                s1.pop()
            else:
                s1.append(i)
        t1 = []
        for i in t:
            if i == '#':
                if not t1:
                    continue
                t1.pop()
            else:
                t1.append(i)
            
        return s1 == t1


# backward comparation: time n space 1
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 不可以在遇到'#'时直接让指针位移2格，因为可能有两个'#'相连的情况
        # 如果直接记录有多少个'#'的话又不满足space O(1)
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0 # how many steps to go back
        while True:
            # 使用while循环来一直走到不需要后退为止
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1 # 如果当前back不为0或者出现新的'#'，则一直后退
                i -= 1 # 后退
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            # 两者都退到不需要再退的时候去比较当前的char
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                # 如果走不到index=-1，则返回False
                return i == j == -1
            i, j = i - 1, j - 1