class Solution:
    def countAndSay(self, n: int) -> str:
        # The sequence starts with "1"
        s = "1"

        # Build the sequence n-1 more times
        for _ in range(n - 1):
            s = self.nextTerm(s)

        return s

    def nextTerm(self, s: str) -> str:
        result = []
        i = 0
        n = len(s)

        # Run-length encode the string
        while i < n:
            count = 1
            # Count how many times s[i] repeats
            while i + 1 < n and s[i] == s[i + 1]:
                count += 1
                i += 1
            
            # Append "count + digit"
            result.append(str(count))
            result.append(s[i])

            i += 1

        return "".join(result)
