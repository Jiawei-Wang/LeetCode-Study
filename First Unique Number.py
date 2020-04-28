class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.dict = {}
        for i in nums:
            self.add(i)

    # 这个dictionary就是普通的dictionary，将每个元素出现次数记录下来
    # 重点在这个queue，因为不断使用add，所以只要被判断出现2次或以上的元素，在下一次使用showFirstUnique时就不需要再判断了，所以只要保留上一次showFirstUnique时的答案，从它开始往后找就行了
    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.dict[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def add(self, value: int) -> None:
        if value in self.dict:
            self.dict[value] += 1
        else:
            self.dict[value] = 1
            self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
