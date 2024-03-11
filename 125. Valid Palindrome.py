class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 重点不是验证palindrome，而是学习清理string
        """
        1. 大写改小写
        2. 去掉空格
        # 几种常见的增删空格方法：
        # https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
        3. 去掉标点
        # 几种常见的去除标点方法：
        # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
        """
        lower = s.lower()
        no_space = lower.replace(" ", "") 
        no_pun = no_space.translate(no_space.maketrans('', '', string.punctuation))

        return no_pun[:len(s)//2] == no_pun[::-1][:len(s)//2]
        
        """
        对帖子的学习：https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
        四种去标点方法：

        import re, string

        s = "string. With. Punctuation"
        exclude = set(string.punctuation)
        regex = re.compile('[%s]' % re.escape(string.punctuation))

        # 由快到慢：
        def test_trans(s):
            return s.translate(str.maketrans('', '', string.punctuation))
            
        def test_re(s):  # From Vinko's solution, with fix.
            return regex.sub('', s)            
            
        def test_set(s):
            return ''.join(ch for ch in s if ch not in exclude)

        def test_repl(s):  # From S.Lott's solution
            for c in string.punctuation:
                s=s.replace(c,"")
            return s
            
        s.translate(None, string.punctuation) # 旧版
        s.translate(str.maketrans('', '', string.punctuation)) # 新版
        
        import string
        a = string.punctuation
        print(a)
        !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        
        maketrans() and translate():
        https://www.w3schools.com/python/ref_string_maketrans.asp
        https://www.w3schools.com/python/ref_string_translate.asp
        """

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return clean_string == clean_string[::-1]