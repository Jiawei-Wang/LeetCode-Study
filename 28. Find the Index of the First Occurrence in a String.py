# built in
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# m*n
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


# KMP: m+n
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # 1. build LPS: m
        # For a pattern P, LPS[i] is the length of the longest 
        # proper prefix of P[0...i] which is also a suffix of P[0...i]
        # while is also not equal to the full string.
        # for example "ababc"
        # LPS = [0, 0, 1, 2, 0]
        # first char "a" is not a proper prefix so LPS[0] = 0
        # LPS[3] = 2 means longest proper prefix of "abab" is "ab"
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0  # length of the previous longest prefix suffix

            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]  # fall back in pattern
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        lps = build_lps(needle)

        # 2. Search using KMP: n
        i = j = 0  # i for haystack, j for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j  # Match found
            else:
                if j != 0:
                    j = lps[j - 1]  # Use LPS to skip characters
                else:
                    i += 1
        
        return -1  # No match found