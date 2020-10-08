class Solution:
    # 直接使用insert
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target =[]
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target

    # 每次都把list重新拼接
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target =[]
        for i in range(len(nums)):
            if index[i] == len(target) :
                target.append(nums[i])
            else:
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target
