class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for i in text:
            if i in ans:
                if i == 'l' or i == 'o':
                    ans[i] += 0.5
                else:
                    ans[i] += 1
                    
        return int(min(ans.values()))


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter('balloon')
        return min([cnt[c] // cntBalloon[c] for c in cntBalloon])


# 2024
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        balloon:
        a: 1
        b: 1
        n: 1
        l: 2
        o: 2
        """

        hashmap = {"a":0, "b":0, "n":0, "l":0, "o":0}

        for char in text:
            if char in hashmap:
                hashmap[char] += 1
        
        answer = float('inf')
        for key, value in hashmap.items():
            if key == "l" or key == "o":
                answer = min(answer, value//2)
            else:
                answer = min(answer, value)
        return answer