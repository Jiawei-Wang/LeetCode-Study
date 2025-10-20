class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {char: 0 for char in 'abc'}
        res = 0
        left = 0
        for right in range(len(s)): 
            count[s[right]] += 1
            while all(count.values()): # while all values in count are true
                count[s[left]] -= 1
                left += 1
            res += left
        return res

        # in the beginning the requirement is not satisfied (all(count.values()) == True)
        # so left pointer will stay at 0 
        # then when right pointer moves into position where the requirement is satisfied
        # we start to move left pointer to meet the minimum requirement
        # so every substring from s[0:right] to s[left:right] all meet requirement
        # and we do this for every right pointer position