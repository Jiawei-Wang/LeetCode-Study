class Solution:
    # brute force
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        for i in words:
            for j in words[words.index(i)+1:]:
                new_i = set(i)
                count = True
                for element in j:
                    if element in new_i:
                        count = False
                if count == True:
                    ans = max(ans, len(i) * len(j))
        return ans
