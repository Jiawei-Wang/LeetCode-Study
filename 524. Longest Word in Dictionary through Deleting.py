class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # sort dict by (first longest length, then lexicographical)
        def by_length(string):
            return (-len(string), string)
        sorted_dict = sorted(dictionary, key=by_length)

        # check if A can transform into B by deleting chars
        def can_transform(A, B):
            index = 0 
            for char in B:
                index = A.find(char, index)
                # s.find(c, i): find the index of the first occurrence of char c in string s[i:]
                # return the index or -1 
                if index == -1:
                    return False
                index += 1
            return True

        for word in sorted_dict:
            if can_transform(s, word):
                return word        
        return ""


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        length = len(s)
        
        def is_in(word):
            i = 0
            j = 0

            while i <= len(word) and j <= length:
                if i == len(word) and j == length:
                    return True
                elif j == length:
                    return False
                elif i == len(word):
                    return True
                
                if word[i] == s[j]:
                    i += 1
                
                j += 1

            return False
        
        # first sort by length, longer ones first
        # then for same length, sort by lexicographical order
        dictionary.sort(key = lambda x : (-len(x), x))
        for word in dictionary:
            if is_in(word):
                return word
        
        return ""
