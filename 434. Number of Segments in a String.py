class Solution:
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                segment_count += 1

        return segment_count