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
        
