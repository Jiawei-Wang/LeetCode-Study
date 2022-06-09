# 读题后感想：decision tree，对于每个元素有两个选择，加入list，或者不加，最后查看sum of list是否是sum of nums的一半
# 因为每个元素都是正整数，所以如果当前sum > sum of nums的一半时，可以停止当前tree branch
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum of nums首先必须是个2的倍数
        total = sum(nums)
        if total % 2:
            return False
        
        # 对于一个元素而言，我们关心的是它的下标（走到哪了），当前总和，以及target（这道题是sum(nums)//2)
        def add(index, cur, target):
            # 首先检查走到头（即上一轮是最后一个元素，已经选择加入或者不加入）的情况
            if index == len(nums) and cur != target:
                return False
            
            if cur > target:
                return 
            elif cur == target:
                return True
            
            return add(index+1, cur+nums[index], target) or add(index+1, cur, target)

        return add(0, 0, total//2)
    
"""
decision tree超时
"""


"""
dp: 将问题转化为subproblem
对于nums[:-1]，是否可以找到一个list，其sum为 sum(nums)//2 或者 sum(nums)//2-nums[-1]
从尾部去掉的元素数量越多，从头部开始的sublist所拥有的可能的target就越多，所以用一个set去保存
set中已有的元素不需要更新或者删除，举例：[1,2,3,4]
对于[1,2,3,4]而言，target = [5] (这4个元素是否可以组成5)
对于[1,2,3]而言，target = [5, 1] (选择4和不选择4，剩下3个元素是否可以组成5或者1)
对于[1,2]而言，target = [5, 1, 2, -2] (选择4和3，选择4，选择3，都不选择)


下面的解法是bottom up，记录当前总和，如果总和中出现sum(nums)//2，则返回True
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
         
        dp = set()
        dp.add(0) # 不选择任何元素时所有可以获得的值只有一个：0
        
        for i in range(len(nums)): # 正序反序没有任何影响
            cur = set() # 在循环的过程中不能对set进行修改，所以要创建一个新的
            for value in dp:
                cur.add(value)
                if value + nums[i] < target:
                    cur.add(value+nums[i])
                elif value + nums[i] == target:
                    return True
            dp = cur
            
        return False