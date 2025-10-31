class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        array = s.split(" ")
        curr = -float("inf")
        for word in array:
            if "0" <= word[0] <= "9":
                if int(word) > curr:
                    curr = int(word)
                else:
                    return False
        return True
