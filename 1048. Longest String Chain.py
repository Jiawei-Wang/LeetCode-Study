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


# more optimal
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)  
        dp = {}
        best = 1

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            best = max(best, dp[word])

        return best


# 2025
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        hashmap = defaultdict(int)
        
        min_length = min([len(word) for word in words])
        for word in words:
            length = len(word)

            if length == min_length:
                hashmap[word] = 1
                continue
            
            best = 1
            for index in range(length):
                new_word = word[0:index] + word[index+1:]
                if new_word in hashmap:
                    best = max(best, hashmap[new_word]+1)
            hashmap[word] = best
            
        return max(hashmap.values())
