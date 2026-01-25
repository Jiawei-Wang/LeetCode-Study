# divide n objects into 3 groups, each group can have 0 <= x <= limit objects
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if 3 * limit < n: return 0  # Impossible to distribute
        if 3 * limit == n: return 1 # Only one way when exactly limit for all

        # put 2 dividers between n objects
        allCases = ((n+2)*(n+1))//2  # Total unrestricted ways

        # Compute cases where at least one child gets more than limit candies
        excludeOne = (n - (limit + 1) + 2)
        oneLimit = 3 * ((excludeOne * (excludeOne - 1)) // 2) if excludeOne > 1 else 0

        # Compute cases where at least two children get more than limit candies
        excludeTwo = (n - 2 * (limit + 1) + 2)
        twoLimit = 3 * ((excludeTwo * (excludeTwo - 1)) // 2) if excludeTwo > 1 else 0

        # Compute cases where all three children get more than limit candies
        excludeThree = (n - 3 * (limit + 1) + 2)
        threeLimit = ((excludeThree * (excludeThree - 1)) // 2) if excludeThree > 1 else 0

        # Apply Inclusion-Exclusion Principle
        return allCases - oneLimit + twoLimit - threeLimit