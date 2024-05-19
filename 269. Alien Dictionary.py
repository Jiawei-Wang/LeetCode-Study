"""
in English: a < b < c < ... < z
in this question, order of letters is unknown
we are given an input: a sorted list of strings
we need to give output: a sorted string of all letters 

for example: 
words = ["wrt", "wrf", "er", "ett", "rftt"]
we know:
1. t < f (wrt < wrf)
2. w < e (wrf < er)
3. r < t (er < ett)
4. e < r (ett < rftt)
so we know the order of all 5 letters
w < e < r < t < f
we return wertf

so we can translate this question into:
1. build the directed graph
2. check if there is a circle in graph
3. if no circle, return a valid order
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # first build adj list for all letters
        # a: (b, c, d): b, c, d are bigger than a
        adj = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            # the only way to find order of letters is to check one by one
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # corner case: if abcd > abc we know there is no right answer
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # now we know w1[j] < w2[j]
                    adj[w1[j]].add(w2[j]) 
                    break

        # then check for circle
        visited = {} # key: letter, value: bool, 
        # False: already visited, True: currently being visited
        res = []

        def dfs(char):
            if char in visited:
                return visited[char] # if True, we find a circle

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            # for dfs, we go all the way to end of path, and append that char first
            # so when we return back to current dfs, current char is in front of that char
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)