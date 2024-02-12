class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        t1 = sorted(s1)
        t2 = sorted(s2)

        small = min(t1, t2)
        big = max(t1, t2)

        for i in range(len(small)):
            if big[i] < small[i]:
                return False
        return True


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26  # Array to count occurrences of characters in s1
        count2 = [0] * 26  # Array to count occurrences of characters in s2

        # Count occurrences of characters in s1
        for char in s1:
            count1[ord(char) - ord('a')] += 1

        # Count occurrences of characters in s2
        for char in s2:
            count2[ord(char) - ord('a')] += 1

        # Variables to track if s1 can break s2 and vice versa
        can_break_s1 = True
        can_break_s2 = True

        # Check if s1 can break s2
        diff = 0
        for i in range(26):
            diff += count1[i] - count2[i]
            if diff < 0:
                can_break_s1 = False
                break

        # Check if s2 can break s1
        diff = 0
        for i in range(26):
            diff += count2[i] - count1[i]
            if diff < 0:
                can_break_s2 = False
                break

        # Return True if either s1 can break s2 or s2 can break s1
        return can_break_s1 or can_break_s2
