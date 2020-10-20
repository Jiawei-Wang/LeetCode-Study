"""
Amazon OA2 2020
find the maximum number of unites of any mix of products that can be shipped
https://leetcode.com/discuss/interview-question/793606/
input:
    num: an integer representing number of products
    boxes: a list of integers representing the number of available boxes for products
    unitSize: an integer representing size of unitsPreBox
    unitsPerBox: a list of integers representing the number of units packed in each box
    truckSize: an integer representing the number of boxes the truck can carry
output:
    return an integer representing the maximum units that can be carried by the truck
"""

"""
Input:
    1. num, number of products
    2. boxes, a list of integers representing the number of available boxes for products
    3. unitSize, an integer representing size of unitsPerBox
    4. unitsPerBox, a list of integers representing the number of units packed in each box
    5. truckSize, an integer representing the number of boxes the truck can carry
Output:
    return an integer representing the maximum units that can be carried by the truck
Constraints:
    1 <= |boxes| <= 10^5
    |boxes| == |unitsPerBox|
    1 <= boxes[i] <= 10^7
    1 <= i < |boxes|
    1 <= unitsPerBox[j] <= 10^5
    1 <= j < |unitsPerBox|
    1 <= truckSize <= 10^8
Example:
    Input:
        num = 3
        boxes = [1, 2, 3]
        unitSize = 3
        unitsPerBox = [3, 2, 1]
        truckSize = 3
    Output:
        7
    Explanation:
        product0: 1 box with 3 units
        product1: 2 boxes with 2 units each
        product2: 3 boxes with 1 unit each
"""

# 解法: 使用PQ, 先用unitsPerBox大的物品填充, 用完后再用第二大的, 以此类推直到truckSize为0
import heapq

class Solution():
    def maxUnits(self, num, boxes, unitSize, unitsPerBox, truckSize):
        heap = []

        for i in range(num):
            units_per_box = unitsPerBox[i]
            heapq.heappush(heap, (-units_per_box, boxes[i]))

        ret = 0
        while truckSize > 0 and heap:
            curr_max = heapq.heappop(heap)
            max_boxes = min(truckSize, curr_max[1])
            truckSize -= max_boxes
            ret += max_boxes * (curr_max[0] * -1)
        
        return ret


# test cases
if __name__ == "__main__":
    # should return 7
    case1 = Solution()
    print(case1.maxUnits(3, [1,2,3], 3, [3,2,1], 3))

    # should return 19
    case2 = Solution()
    print(case2.maxUnits(3, [2,5,3], 3, [3,2,1], 50))

    # should return 34
    case3 = Solution()
    print(case3.maxUnits(5, [7, 1, 5, 2, 3], 5, [3, 7, 1, 3, 2], 10))