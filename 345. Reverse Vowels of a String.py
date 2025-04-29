class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        S = list(s)
        i, j = 0, len(S) - 1
        while i < j:
            if S[i] not in vowels:
                i += 1
                continue
            if S[j] not in vowels:
                j -= 1
                continue
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
        return ''.join(S)