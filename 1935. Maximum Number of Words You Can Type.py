class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        keys = {char for char in brokenLetters}

        left = len(words)
        # for word in words:
        #     for key in keys:
        #         if key in word:
        #             left -= 1
        #             break
        # return left

        for word in words:
            for char in word:
                if char in keys:
                    left -= 1
                    break
        return left

