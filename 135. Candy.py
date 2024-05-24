class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        if size <= 1:
            return size

        num = [1] * size

        # first loop makes sure child with a higher rating get more candy than its left neighbor
        for i in range(1, size):
            if ratings[i] > ratings[i - 1]:
                num[i] = num[i - 1] + 1

        # second loop makes sure child with a higher rating get more candy than its right neighbor
        for i in range(size - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                num[i - 1] = max(num[i] + 1, num[i - 1])

        result = sum(num)
        return result
        