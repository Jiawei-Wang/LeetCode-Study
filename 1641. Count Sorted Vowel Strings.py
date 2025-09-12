# change the wording of the question:
# pick a vow, then the next pick can only be this vow or any vow behind it
# do it n times, see how many different combo
# this is the same as the math question:
# we have n indistinguishable balls, distribute them into 5 ordered bins
# for example 2 balls, then we can pick any bin for first ball
# but only bins behind that bin for second ball
# formula for distributing n identical balls into k distinct bins:
# (n+k-1)! / ( n! * (k-1)! )
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # (n+4)! / ( n! * 4!) )
        return (n+4) * (n+3) * (n+2) * (n+1) // 24


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # built in
        return comb(n+4, 4)