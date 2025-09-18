class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)

        dp = defaultdict(int)

        def dfs(word):
            if word not in words:
                return 0
            score = 1
            if dp[word]:
                return dp[word]
            for i in range(len(word)):
                new = word[:i] + word[i+1:]
                score = max(score, dfs(new)+1)
            dp[word] = score
            return score
        
        answer = 0
        for word in words:
            answer = max(answer, dfs(word))
        return answer
