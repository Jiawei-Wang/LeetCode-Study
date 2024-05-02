# time n space 1
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0] * 26 # 记录每个task出现的次数
        Max = 0 # 在遍历tasks时用Max随时更新当前counter中所有元素的最大值（即所有task中出现次数最多的是多少）
        maxCount = 0 # 在遍历tasks时用maxCount随时更新当前counter中最大值对应的下标有几个（即有几个task出现次数并列当前最多）
        
        for task in tasks:
            counter[ord(task)-ord('A')] += 1
            if Max == counter[ord(task)-ord('A')]:
                maxCount += 1
            elif Max < counter[ord(task)-ord('A')]:
                Max = counter[ord(task)-ord('A')]
                maxCount = 1
        
        partCount = Max - 1 # 单个task最多出现Max次，那么中间就有Max-1个间隔段落
        partLength = n - (maxCount - 1) # 假设n=4，maxCount=3，那么就会出现下面的情况：A B C 空 空 A B C 空 空 A B C
        emptySlots = partCount * partLength # 一共有多少个空白位置（位于A第一次出现，和A最后一次出现之间）可供出现次数小于max的task插入，举例：A B C 空 空 A B C 空 空 A B C，那么就是4个空位
        availableTasks = len(tasks) - Max * maxCount
        idles = max(0, emptySlots - availableTasks) # 找出来将其他所有task插入后，还剩多少个空位
        return len(tasks) + idles