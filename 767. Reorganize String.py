import math
class Solution:
    def reorganizeString(self, s: str) -> str:
        length = len(s)

        # first build counter and also get max_count
        counter = dict()
        max_count = 0
        for char in s:
            counter[char] = counter.get(char, 0) + 1
            max_count = max(counter[char], max_count)
        if max_count > math.ceil(length/2):
            return ""

        # then use counter to build freq list
        freq = [[] for _ in range(max_count+1)] 
        for key, value in counter.items():
            freq[value].append(key)
        
        # then put letters into place by using even index first, then odd index
        answer = [None] * length
        pos = 0
        for occurrence in range(max_count, 0, -1):
            letters = freq[occurrence]
            for letter in letters:
                for i in range(occurrence):
                    answer[pos] = letter
                    pos += 2
                    if pos >= length: # when we finish all even index, we start from 1 again
                        pos = 1
        
        return "".join(x for x in answer)




        