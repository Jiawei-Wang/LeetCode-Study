# build-in function
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums)) # 先把integer转变为string
        cmp = lambda x, y: ((x+y) > (y+x)) - ((x+y) < (y+x)) # 因为直接将两个string加起来，看哪个大（数字string之间的比较遵循integer的规则）
        nums = sorted(nums, key=cmp_to_key(cmp)) # 使用自定义规则来sort list
        return str(int(''.join(nums[::-1]))) # 从大到小反向接起来然后输出


# 和built in相同逻辑但从头写代码
class Wrapper:
    def __init__(self, val):
        self.val = str(val)
        
    def __lt__(self, other):
        return int(self.val+other.val) < int(other.val+self.val)
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [Wrapper(n) for n in nums]
        nums.sort(reverse=True)
        nums = [n.val for n in nums]
        
        return str(int(''.join(nums)))


# bubble sort
# 先把顺序排好，然后全部从头到尾接起来
# 同理其他任何sort算法都适用
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))

    # 同样还是定义一个string对比的function
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)