class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubseq(s, word):
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            return i == len(word)
        
        count = 0
        for word in words:
            if isSubseq(s, word):
                count += 1
        return count


# bingo style:
# S keeps moving one char at a time
# every word keeps track of its own progress
class Solution:
    def numMatchingSubseq(self, S, words):
        # example 
        # S = "abcde"
        # words = ["ace", "bd", "a"]

        # first, every word is waiting for first char being matched
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
            # "ace" joins waiting["a"] as iter("ce")
            # "a" joins as iter("")
            # "bd" joins waiting["b"] as iter("d")
        
        # then, go through S
        for c in S:
            # we are at "a" in "abcde"
            for it in waiting.pop(c, ()):
                # we get iter("ce") and iter("")
                waiting[next(it, None)].append(it)
                # waiting["c"] gets iter("e")
                # waiting[None] gets iter("")
                # waiting["b"] is still the same
                # waiting["a"] is no more
        
        # return number of matched words
        return len(waiting[None])



        