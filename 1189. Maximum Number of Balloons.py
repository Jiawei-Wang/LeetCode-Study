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