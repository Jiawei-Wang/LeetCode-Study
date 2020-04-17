class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 暴力解：对于每个元素，都遍历一遍 n^2

        # 改进：先sort，然后每个元素在新序列中的位置即代表小于其的元素总数 nlogn
        '''
        indices = {}
        # 返回的是排序过的list的每个元素（nums中最小的元素新下标为0）
        for idx, num in enumerate(sorted(nums)):
            indices.setdefault(num, idx)
        # 返回一个新list，内容是nums中每个元素在dictionary中的新下标
        return [indices[num] for num in nums]
        '''

        # 再次改进：因为我们知道nums中每个元素都在 0-100的范围内，所以可以进一步缩减sort时间 n
        # 使用 102 防止下标溢出
        count = [0] * 102
        # 在nums中出现的数字，在count中对应下标位置的值则为1
        for num in nums:
            count[num+1] += 1
        # 把截止到i之前的所有出现了的数字的总数记录下来
        for i in range(1, 102):
            count[i] += count[i-1]
        # 将nums中每个数字在count中对应下标的位置的值返回
        return [count[num] for num in nums]
