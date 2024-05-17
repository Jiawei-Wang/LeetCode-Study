# build counter + go through counter
# n^2 + n
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations) + 1
        counter = [0] * length # counter[3] = 5: 5 papers have at least 3 citations

        for cited in citations:
            for i in range(0, min(length, cited+1)):
                counter[i] += 1
        
        answer = 0
        for i in range(length-1, -1, -1):
            answer = max(answer, min(i, counter[i]))
        
        return answer


# build counter + binary search on counter
# n^2 + logn
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo = 0
        hi = len(citations)

        if hi == 1:
            return min(1, citations[0])

        counter = [0] * (hi+1)
        for cited in citations:
            for i in range(0, min((hi+1), cited+1)):
                counter[i] += 1

        # at least number papers with at least number citations
        def is_valid(number):
            return counter[number] >= number

        while lo < hi:
            mid = lo + (hi-lo)//2
            if is_valid(mid) and not is_valid(mid+1):
                return mid
            elif is_valid(mid) and is_valid(mid+1):
                lo = mid + 1
            elif not is_valid(mid):
                hi = mid - 1
        
        return lo


# binary search directly with validation
# nlogn
# validation takes n each time for in total logn times
# building the counter takes n^2, which is actually longer
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo = 0
        hi = len(citations)

        if hi == 1:
            return min(1, citations[0])

        # at least number papers with at least number citations
        def is_valid(number):
            count = 0
            for cite in citations:
                if cite >= number:
                    count += 1
            return count >= number

        while lo < hi:
            mid = lo + (hi-lo)//2
            if is_valid(mid) and not is_valid(mid+1):
                return mid
            elif is_valid(mid) and is_valid(mid+1):
                lo = mid + 1
            elif not is_valid(mid):
                hi = mid - 1
        
        return lo


# bucket sort: O(n)
# improve upon the counter
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n+1)

        # we don't go through 0 to cite to update every value
        # we only update cite
        for cite in citations:
            if cite >= n:
                buckets[n] += 1
            else:
                buckets[cite] += 1
        
        # for example:
        # buckets[5] = 1
        # buckets[4] = 2
        # we know 2 papers have 4 citations, 1 paper has 5 citations
        # so counter[4] = buckets[5] + buckets[4]
        count = 0
        for i in range(n, -1, -1):
            count += buckets[i] 
            if count >= i:
                return i
        
        return 0
        