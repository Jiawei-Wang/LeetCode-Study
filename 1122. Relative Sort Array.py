class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 读题后第一想法：本题要求把arr1中元素按arr2顺序排列，并把剩余元素升序排列，暴力解肯定超时

        # 初始化2D list的方法
        total = [[] for i in range(len(arr2)+1)]

        for i in arr1:
            if i in arr2:
                total[arr2.index(i)].append(i)
            else:
                total[-1].append(i)

        ans = []
        for index in range(len(total)-1):
            # 连接两个list的方法
            ans = ans + total[index]
        ans = ans + sorted(total[-1])
        return ans
    # Time: 6%
    # Space: 100%


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        ans = [] # Hold the resulting relative sort array
        dictionary = {} # Used for counting elements of arr2 that appear in arr1
        diff = [] # Use for tracking elements that don't appear in arr2 but appear in arr1

		# Initialize counts
        for num in arr2:
            if num not in dictionary:
                dictionary[num] = 0

        for num in arr1:
            if num in dictionary:
                dictionary[num] += 1 # Increment count of elements seen
            else:
                diff.append(num) # Add element to difference list (e.g. nums in arr1 not in arr2)

        diff.sort() # Sort the difference

        for num in arr2:
            ans.extend([num] * dictionary[num]) # Add the number of elements seen to  the result set

        ans.extend(diff) # Add the rest of the sorted elements

        return ans
    # Time: 100%
    # Space: 100%
