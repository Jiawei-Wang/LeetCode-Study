# there are even number of piles, and player1 picks first
# so player1 can pick all even index piles or all odd index piles
# for example: 0, 1, 2, 3
# if player1 wants 0 and 2, they can do that
# so they just need to know which one is bigger: sum of all even index piles or sum or all odd index piles
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True