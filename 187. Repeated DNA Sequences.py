class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length <= 10:
            return []

        once = set()
        repeat = set()

        for i in range(length-9): # -9 not -10
            current = s[i:i+10]
            if current in once:
                repeat.add(current)
            else:
                once.add(current)
        
        return list(repeat)