"""
https://leetcode.com/discuss/interview-question/882393/SAP-or-2020
https://leetcode.com/discuss/interview-question/421553/Interview-Question-SAP
"""

# bulit-in 
# time complexity: n^2
class Solution:
    def move(self, n, index, identity):
        ans = []
        for i in range(n):
            curr = identity[i]
            pos = index[i]
            ans.insert(pos, curr) # insert is linear complexity
        return ans

# brute force
# time complexity: n^2
class Solution2:
    def move(self, n, index, identity):
        ans = []
        for i in range(n):
            curr = identity[i]
            pos = index[i]
            ans.append(curr)
            for j in range(len(ans)-1, pos-1, -1):
                ans[j] = ans[j-1]
            ans[pos] = curr
        return ans

TODO
# O(NlogN): AVL tree / Segment tree



if __name__ == "__main__":
    # test case 1: should return [0, 3, 4, 1, 2]
    n = 5
    index = [0, 1, 2, 1 ,2]
    identity = [0, 1, 2, 3, 4]
    case1 = Solution()
    print(case1.move(n, index, identity))
    case12 = Solution2()
    print(case12.move(n, index, identity))

    # test case 2: should return [2, 0, 1]
    n = 3
    index = [0, 1, 0]
    identity = [0, 1, 2]
    case2 = Solution()
    print(case2.move(n, index, identity))
    case22 = Solution2()
    print(case22.move(n, index, identity))