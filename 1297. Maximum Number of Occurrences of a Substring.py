# brute force: check every possible length, check every window for this length
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        answer = 0

        # for every length
        for length in range(minSize, maxSize+1):
            # create a lookup table
            seen = defaultdict(int)

            # build initial window
            occurrence = defaultdict(int)
            for i in range(length):
                occurrence[s[i]] += 1
            
            if len(occurrence) <= maxLetters:
                seen[s[0:i+1]] += 1
            
            # move the window
            for i in range(length, len(s)):
                occurrence[s[i]] += 1
                occurrence[s[i-length]] -= 1
                if occurrence[s[i-length]] == 0:
                    del occurrence[s[i-length]]
                if len(occurrence) <= maxLetters:
                    seen[s[i-length+1:i+1]] += 1

            # seen could be empty so give a default value
            answer = max(answer, max(seen.values(), default=0))

        return answer


# better: only use minSize, keep the rest the same
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        answer = 0

        length = minSize
        
        # create a lookup table
        seen = defaultdict(int)

        # build initial window
        occurrence = defaultdict(int)
        for i in range(length):
            occurrence[s[i]] += 1
        
        if len(occurrence) <= maxLetters:
            seen[s[0:i+1]] += 1
        
        # move the window
        for i in range(length, len(s)):
            occurrence[s[i]] += 1
            occurrence[s[i-length]] -= 1
            if occurrence[s[i-length]] == 0:
                del occurrence[s[i-length]]
            if len(occurrence) <= maxLetters:
                seen[s[i-length+1:i+1]] += 1

        # seen could be empty so give a default value
        answer = max(answer, max(seen.values(), default=0))

        return answer