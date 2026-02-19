# brute force: try all combos: n^3


# better: n^2
# for each number
# count how many smaller numbers on the left and how many bigger numbers on the left
# then bigger on right and smaller on right
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        result = 0

        for j in range(n):
            left_smaller = left_greater = 0
            right_smaller = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_greater += 1
                else:
                    right_smaller += 1

            result += left_smaller * right_greater
            result += left_greater * right_smaller

        return result


# best: Fenwick Tree / BIT can reduce it to nlogn

