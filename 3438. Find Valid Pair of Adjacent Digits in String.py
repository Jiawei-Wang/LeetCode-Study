class Solution:
    def findValidPair(self, s: str) -> str:
        # count
        counter = defaultdict(int)
        for char in s:
            counter[int(char)] += 1
        
        valid = set()
        for key, value in counter.items():
            if key == value:
                valid.add(key)

        # check
        for i in range(len(s)-1):
            pair = s[i:i+2]
            first = int(pair[0])
            second = int(pair[1])
            
            if first != second and first in valid and second in valid:
                return pair
        
        return ""