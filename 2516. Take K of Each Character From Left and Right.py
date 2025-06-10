# change problem to: find the longest substring in the string, 
# so that the rest of the string (could be 2 parts of 1 part depending on
# where the substring starts and ends) meet the requirements
# so this is a sliding window problem
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # count a, b, c in string
        count = [0, 0 ,0]
        for c in s:
            count[ord(c) - ord("a")] += 1
        
        # handle corner case
        if min(count) < k:
            return -1
        
        # sliding window
        res = len(s) # set initial answer to maximum length, then we will find better one to replace it
        left = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord("a")] -= 1

            # every time we move right side by one step
            # we need to update left side so the new window is still valid
            while min(count) < k:
                count[ord(s[left]) - ord("a")] += 1
                left += 1

            # now use valid window to update res
            res = min(res, len(s) - (right-left+1))

        return res