class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(Counter(word).values()) 
        # key: how many times a char has occured in input
        # value: how many chars have the same occurrence

        if (len(cnt) == 1): # every char has the same occurrence
            # if every char occurs once: "abc" -> remove any char -> True
            # if only one char in the whole input: "aa" -> remove one "a" -> True
            return list(cnt.keys())[0] == 1 or list(cnt.values())[0] == 1
        if (len(cnt) == 2):
            # we should have something like:
            # {3: 5, 4: 1} 
            # big occurrence must == small occurrence + 1
            # and big occurrence must have value == 1
            # or 
            # small occurrence is 1 and only one char has it
            # for example: "abbbcccddd" -> remove "a" -> True
            f1, f2 = min(cnt.keys()), max(cnt.keys())
            return (f1 + 1 == f2 and cnt[f2] == 1) or (f1 == 1 and cnt[f1] == 1)
        
        return False
