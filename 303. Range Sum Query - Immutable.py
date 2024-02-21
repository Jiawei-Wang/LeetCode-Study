class NumArray:

    def __init__(self, nums: List[int]):
        self.num = []
        self.total = []
        total = 0
        for num in nums:
            self.num.append(num)
            total += num
            self.total.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.total[right]
        else:
            return self.total[right] - self.total[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)