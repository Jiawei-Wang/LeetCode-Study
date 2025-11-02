# greedy doesn't always guarantee best solution
# because if we greedily pick the cloest next char, the next next char could be very far
# so we need to find the best choice based on previous choices 
# decision tree -> DP
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)

        # we need a quick lookup table
        # key: character in ring, value: all its indices
        char_positions = defaultdict(list)
        for i, ch in enumerate(ring):
            char_positions[ch].append(i)
        
        prev = [float('inf')] * n # prev[j] = minimum steps to have ring aligned at j after typing previous characters
        prev[0] = 0  # Starting at position 0 with no steps taken

        # Process each character in key from first to last
        for ch in key:
            curr = [float('inf')] * n

            # For every position where ring has the current target character
            for pos in char_positions[ch]:
                # Try coming from every previous position
                for j in range(n):
                    if prev[j] < float('inf'):
                        # Calculate rotation distance between j and pos
                        diff = abs(j - pos)
                        rotate_steps = min(diff, n - diff)

                        # Total steps = previous + rotate + button press
                        curr[pos] = min(curr[pos], prev[j] + rotate_steps + 1)

            # Move current row to previous for next iteration
            prev = curr

        # Final answer is the minimum steps over all possible ending positions
        return min(prev)
