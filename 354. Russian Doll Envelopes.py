# binary search 
# similar to 300. Longest Increasing Subsequence but with 2 values each element instead of 1
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # width is increasing, height is decreasing
        # for example: [[3, 5], [6, 7], [7, 13], [6, 10], [8, 4], [7, 11]]
        # we will have: [[3, 5], [6, 10], [6, 7], [7, 13], [7, 11], [8, 4]]

        LIS = []
        size = 0
        for (w, h) in envelopes:

            # if it's the first element, or we find a bigger element, we make it as new tail
            # (when h > LIS[-1], we know we are looking at a new element
            #  with w > last one and h > last one)
            # for example LIS = [5], when h = 10 > 5, we know w of this element > w of element 5
            if not LIS or h > LIS[-1]:
                LIS.append(h)
                size += 1
            
            # if new element is not bigger, we want to see if we can update any tail in LIS
            # for example LIS = [5, 10] and we are now at 7
            # we update the LIS[1] = 7
            else:
                l, r = 0, size
                while l < r:
                    m = l + (r - l) // 2
                    if LIS[m] < h:
                        l = m + 1
                    else:
                        r = m
                LIS[l] = h
                
        return size
