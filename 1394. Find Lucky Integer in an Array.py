class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = [0] * 501
        for a in arr:
            cnt[a] += 1
        for i in range(500, 0, -1):
            if cnt[i] == i:
                return i
        return -1

    # 1. 本题已知最大数字是500，所以cnt的长度有上限
    # 2. 并不需要将cnt排序，只需要反向读取然后输出找到的第一个满足条件的即可，因为数字越大，次数对应也越大
