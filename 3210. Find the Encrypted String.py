class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return s[k%len(s):] + s[0:k%len(s)]