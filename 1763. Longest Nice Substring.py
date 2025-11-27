class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Helper function
        def dfs(sub):
            if len(sub) < 2:
                return ""

            chars = set(sub)

            for i, c in enumerate(sub):
                if c.swapcase() not in chars:  # invalid splitter
                    # solve left and right parts
                    left  = dfs(sub[:i])
                    right = dfs(sub[i+1:])
                    return left if len(left) >= len(right) else right

            # whole substring is nice
            return sub

        return dfs(s)
