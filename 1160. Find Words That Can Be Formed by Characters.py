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


# 2024
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)

        def contains(word):
            w = Counter(word)
            for key, value in w.items():
                if key not in count:
                    return False
                elif value > count[key]:
                    return False
            return True

        answer = 0
        for word in words:
            if contains(word):
                answer += len(word)
        return answer
