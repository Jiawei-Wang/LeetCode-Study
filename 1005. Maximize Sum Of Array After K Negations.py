class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        # assume m negative ints
        # if m>=k: just change first k negative ints to positive
        # if m<k: change all negative to positive, then change the new smallest non-negative int 0 or 1 time
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2
        """
        if m>=k: i will be equal to k so just return new sum(A)
        if m<k: i will point to last negative int, we change the new smallest non-negative int (K-i)%2 time 
        """