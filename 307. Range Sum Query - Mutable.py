class NumArray:
    # O(1)
    def __init__(self, nums: List[int]):
        self.nums = nums

    # O(1)
    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    # O(n)
    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = []
        self.total = []
        total = 0
        for num in nums:
            self.nums.append(num)
            total += num
            self.total.append(total)
        self.length = len(self.nums)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        for i in range(index, self.length):
            self.total[i] += diff
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.total[right] - self.total[left-1] if left >= 1 else self.total[right]  