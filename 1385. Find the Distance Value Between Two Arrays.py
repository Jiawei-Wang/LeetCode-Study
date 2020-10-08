class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # 对问题的理解：对于arr1中每个元素，如果arr2中每个元素和它距离都大于 d，则count += 1
        # 想法：两重循环的暴力解肯定超出时间限制，所以思考时间复杂度尽可能低的算法

        # 先遍历arr2得到合法元素的范围，然后去arr1里找是否存在合法元素
        legal = set()
        for i in arr2:
            low = i - d
            high = i+d
            for number in range(low, high+1):
                legal.add(number)

        count = 0
        for i in arr1:
            if i not in legal:
                count += 1
        return count
    # Time: 23%
    # Space: 100%


# 此解法的核心在于sort，在sort完之后只需要两个pointer就可以进行排除
# arr1中每一个元素，只需要满足在一个arr2的元素的范围内，即可被排除
# 所以对于arr1的每个元素来说，只需要找到它夹在arr2两个元素的范围之外即可
# 对于arr2的每个元素来说，如果它已经被上一个arr1的元素排除，下一个arr1的元素也不需要再去i对比
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0

        while i < len(arr1) and j < len(arr2):
            # 如果arr2的当前元素不大于arr1的当前元素
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1

            # 如果arr2的当前元素大于arr1的当前元素
            else:
                # 如果超出范围，则count += 1
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1

        dist += len(arr1) - i
        return dist
    # Time: 92%
    # Space: 100%
