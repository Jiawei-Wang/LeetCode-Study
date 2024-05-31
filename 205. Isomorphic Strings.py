# below answer is incorrect: 
# s = "badc"
# t = "baba"
# return value is True
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         length = len(s)
#         len_t = len(t)
#         if length != len_t:
#             return False
#         hashmap = dict()
#         for i in range(length):
#             char = s[i]
#             if char not in hashmap:
#                 hashmap[char] = [i]
#             else:
#                 hashmap[char].append(i)
#         new = [0] * length
#         for i in range(length):
#             target = hashmap[s[i]]
#             char = t[i]
#             for index in target:
#                 new[index] = char
#         return "".join(x for x in new) == t


# All occurrences of a character must be replaced with another character 
# while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.
# for example: e can be mapped to any char, including e, then other chars cannot be mapped to this char again

# solution 1: get rid of chars completely 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length = len(s)

        def check(string):
            res = []
            count = dict()
            for index in range(length):
                char = string[index]
                if char in count:
                    count[char].append(index)
                else:
                    count[char] = [index]

            # dictionary maintains insertion order
            # so as long as no modification happens between iteration
            # this line will always return in the same order
            for key, value in count.items(): 
                res.append(value)
            return res

            # so for string "abccba"
            # res = [[0, 5], [1, 4], [2, 3]]
            # meaning: first char occurs at 0 and 5
            # second char occurs at 1 and 4
            # etc
        
        return check(s) == check(t)


# solution 2: check last occurrence
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = [0] * 256, [0] * 256 # ASCII size is 256
        n = len(s)
        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]:  
                return False
            m1[ord(s[i])] = i + 1 
            m2[ord(t[i])] = i + 1 
        return True