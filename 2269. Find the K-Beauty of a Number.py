class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string = str(num)
        counter = 0
        for i in range(len(string)-k+1):
            substring = int(string[i:i+k])
            if substring != 0 and num % substring == 0:
                counter += 1
        return counter