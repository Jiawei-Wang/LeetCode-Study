"""
decision tree: for every rod, there are 3 options:
add it to left, add it to right, skip it
O(3^n)

but we don't need the full information, we only care about the current height of left and right
possible different heights are too many, we store the height differences instead

create the state:
dp[diff] = maximum height of the shorter support, given the height difference diff

create the transition:
For each existing state (diff, shorter_height):
1. if new rod is added to left:
new_diff = diff + rod
new_shorter stays the same (shorter side does not change)
2. if new rod is added to right:
new_diff = abs(diff - rod)
if rod <= diff:
    new shorter side height = shorter_height + rod
else:
    new shorter side height = shorter_height + diff
3. If we skip the rod:
No change to diff or shorter height.
"""
class Solution:
    def tallestBillboard(self, rods):
        # dp[diff] = max height of the shorter side
        dp = {0: 0}

        for rod in rods:
            # Copy current states so updates do not interfere within this iteration
            next_dp = dp.copy()

            for diff, short_height in dp.items():

                # --- Option 1: Add rod to the left side ---
                new_diff = diff + rod
                next_dp[new_diff] = max(
                    next_dp.get(new_diff, 0),
                    short_height
                )

                # --- Option 2: Add rod to the right side ---
                if rod <= diff:
                    # Right side is extended, left stays shorter
                    new_diff = diff - rod
                    new_short = short_height + rod
                else:
                    # Right becomes taller; diff flips
                    new_diff = rod - diff
                    new_short = short_height + diff
                
                next_dp[new_diff] = max(
                    next_dp.get(new_diff, 0),
                    new_short
                )

                # --- Option 3: Skip rod ---
                # Already implicitly handled because next_dp started as dp.copy()

            dp = next_dp

        return dp.get(0, 0)
