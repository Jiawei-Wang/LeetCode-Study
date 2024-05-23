"""
question: find number of combinations [string a, string b] from list ideas that are valid
requirement: new string a[0]+b[1:] and new string b[0]+a[1:] both cannot exist in ideas
constraints:
1. all strings in ideas are unique
2. [string a, string b] != [string b, string a]

solution 1: brute force: 
for all combinations, verify if any of the 2 new strings is in ideas
O(n^2)

solution 2: 
for example: [coffee, chord, come, boffee, bee, buffalo]
1. create a set for each prefix (first letter)
    c = {offee, hord, ome}
    b = {offee, ee, uffalo}
2. two suffix within same set cannot be combined
3. two suffix from different sets can only be combined if suffix doesn't exist in the other set
4. so invalid: coffee, boffee, valid: chord, come, bee, buffalo
5. 2 * 2 * 2 = 8
"""
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        A = [set() for _ in range(26)]
        for idea in ideas:
            A[ord(idea[0]) - ord('a')].add(idea[1:])
        # for example: idea = coffee
        # A[2] = {offee}

        ans = 0
        for i in range(25): # for a prefix set
            for j in range(i+1, 26): # check all other prefix sets
                duplicate = len(A[i] & A[j]) # set & set: return a set of elements in both sets
                ans += 2 * (len(A[i]) - duplicate) * (len(A[j]) - duplicate)

        return ans
        
