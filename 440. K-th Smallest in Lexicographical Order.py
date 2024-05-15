"""
1. this is a preorder traversal on a denary tree
   root 0 has 9 children: [1, 9]
   1 has 10 children: [10, 19]
   10 has 10 children: [100, 109]
   ...
   the tree has infinite depth 
2. so finding the k-th element in range [1, n] means that:
    1) we start from node 1 not root 0
    2) the path from 1 to n is defined: 
       for example: from 1 to 25: 1 -> 10 -> 19 -> 2 -> 20 -> 25
    3) and we pick the one that has k steps from 1
3. from the example above we know, since n is fixed, the depth of the tree is finite
   (we will never need to go down 10 -> 100 or 19 -> 190)
   therefore the distance between a node and its right side same level node is finite
   (one step from 10 to 11, ten steps from 1 to 2)
4. so we don't need to traverse the tree, we just need to know where to go and calculate how far it is
5. to make things even easier, we have only two moves: 
    1) one level down: for example 55 -> 550 
    2) right side same level: for example 55 -> 56
    (99 -> 100 doesn't matter since it has same steps as 55 -> 56)
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # get distance between cur and its right side same level node 
        def calDistance(cur): 
            distance = 0
            right = cur + 1 
            while cur <= n:
                distance += min(n + 1, right) - cur
                cur *= 10
                right *= 10
            return distance
            """
            for example to go from 5 to 6, n = 170
            it would be: 5 -> 50 (since 50 < 170 < 500) -> 59 -> 6
            """

        cur = 1
        k -= 1
        while k > 0:
            distance = calDistance(cur)
            if distance <= k:
                cur += 1
                k -= distance
            else: # if we cannot move to right node, that means target is deeper in the tree
                # then we move 1 step down the tree
                cur *= 10 
                k -= 1
        return cur

 