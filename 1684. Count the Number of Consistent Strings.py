class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set([char for char in allowed])
        count = 0
        for word in words:
            consistent = True
            for char in word:
                if char not in allow:
                    consistent = False
                    break
            count += consistent
        return count
            
                