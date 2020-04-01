class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def check(word):
            charList = list(chars)
            for char in word:
                if char in charList:
                    charList.remove(char)
                else:
                    return False
            return True


        ans = 0
        for word in words:
            if check(word):
                ans += len(word)
        return ans
