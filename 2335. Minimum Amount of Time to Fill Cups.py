class Solution:
    def fillCups(self, A: List[int]) -> int:
        """
        res >= max(A)
        Because each time,
        one type can reduce at most 1 cup,
        so the final result is bigger or equal to max(A)

        res >= ceil(sum(A) / 2)
        Because each time,
        we can fill up to 2 cups,
        so the final result is bigger or equal to ceil(sum(A) / 2)

        best strategy to achieve the best possible result
        greedily fill up 2 cups with different types of water.
        Each step, we pick the 2 types with the most number of cups
        until there is only one kind.
        """
        return max(max(A), (sum(A) + 1) // 2)