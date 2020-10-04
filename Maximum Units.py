"""
Amazon OA2 2020
find the maximum number of unites of any mix of products that can be shipped
https://leetcode.com/discuss/interview-question/793606/
input:
    num: an integer representing number of products
    boxes: a list of integers representing the number of available boxes for products
    unitSize: an integer representing size of unitsPreBox
    unitsPerBox: a list of integers representing the number of units packed in each obx
    truckSize: an integer representing the number of boxes the truck can carry
output:
    return an integer representing the maximum units that can be carried by the truck
"""

# 解法: 使用PQ, 先用unitsPerBox大的物品填充, 用完后再用第二大的, 以此类推直到truckSize为0
import heapq

def maxUnits(num, boxes, unitSize, unitsPerBox, truckSize):
    heap = []

    for i in range(len(boxes)):
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
print(maxUnits(3, [1,2,3], 3, [3,2,1], 3))
print(maxUnits(3, [2,5,3], 3, [3,2,1], 50))