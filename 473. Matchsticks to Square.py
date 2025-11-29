class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        
        # Square requires total sum divisible by 4
        if total % 4 != 0:
            return False
        
        side = total // 4

        # Sort descending for better pruning (big sticks first)
        matchsticks.sort(reverse=True)

        # If the largest stick is longer than a side → impossible
        if matchsticks[0] > side:
            return False

        # 4 sides initialized to 0
        sides = [0] * 4

        def backtrack(i):
            # If we've placed all sticks successfully
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side

            stick = matchsticks[i]

            for s in range(4):
                # If placing the stick in side s doesn't exceed target
                if sides[s] + stick <= side:
                    sides[s] += stick

                    if backtrack(i + 1):
                        return True

                    # Backtrack
                    sides[s] -= stick

                # PRUNE: If this side is 0, placing on other empty sides is redundant
                if sides[s] == 0:
                    break

            return False

        return backtrack(0)
