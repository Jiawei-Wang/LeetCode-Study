# if we sort the arrays using the first element of each array
# we are only sure the topleft element is the smallest element
# we still don't know where the biggest element is and still need to go through every array
# so sorting is not needed
# but on the other hand, regardless of sorting, we know where smallest and biggest elements are on each array
# so just compare them with the previous ones
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0 # it is not biggest - smallest because the question asks max_distance for two elements from two different arrays

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance