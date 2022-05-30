# greedy
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果走一圈可获得的汽油总数小于汽油消耗总数，则不可能完成一圈
        if sum(gas) < sum(cost):
            return -1
        
        total = 0 # 遍历时总共积累的汽油净增
        start = 0 # 从第一个元素开始遍历
        for i in range(len(gas)):
            total += (gas[i] - cost[i]) # 每走一步获得的汽油净增
            
            if total < 0: # 如果从start开始到i为止的汽油净增为负，则start移至i下一个元素
                total = 0
                start = i + 1
        
        return start
    
    """
    理解for loop：
    1. 如果题目有解，则有且必只有一个解（题目原话），所以肯定有返回值
    2. 从start开始走到i时发现total < 0说明：
             1）因为每走一步都在检查total是否<0，所以肯定是i这一步负数过大导致
             2）而从start开始每一步total一直都是正数，或者起码等于0
             3）可以推断出来从start到i，其中任意一个位置j开始走到i，汽油净增肯定都不会大于从start到i（因为从start到j的total >=0)
             4）进而可知从start到i都不符合要求，那么答案肯定在i+1到末尾之间
    """