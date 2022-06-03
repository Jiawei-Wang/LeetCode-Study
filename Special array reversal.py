# given a string, reverse all letters without touching any special chars in it

# 3 arrays: one for letters, one for index of letters, one for special chars
# time n space n
class Solution:
    def reverse(self, s):
        # code here
        if not s:
            return ''
            
        letter = []
        index = []
        special = []
        for i in range(len(s)):
            # char.isalpha()
            if s[i].isalpha():
                letter.append(s[i])
                index.append(i)
            else:
                special.append(s[i])
        
        letter.reverse()
        
        for i in range(len(letter)):
            position = index[i]
            # list.insert(index, value)
            special.insert(position, letter[i])
        
        return ''.join(special)


# two pointer
# split into a list, two pointer through list, back to string
# time n space n
class Solution:
    def reverse(self, s):
        # code here
        char = [c for c in s]
        i = 0
        j = len(char) - 1
        while i < j and i < len(char) and j >= 0:
            if not char[i].isalpha():
                i += 1
                continue
            if not char[j].isalpha():
                j -= 1
                continue
            char[i], char[j] = char[j], char[i]
            i += 1
            j -= 1
        return ''.join(char)