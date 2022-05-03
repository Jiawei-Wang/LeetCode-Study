class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer: time n space 1
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dictionary: time n space n
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search: time nlogn space 1
        for i in range(len(numbers)): # for loop的意义是对于每个元素，都去寻找是否有匹配元素
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2 # 使用 左+(右-左)//2 的方式来防止overflow
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1