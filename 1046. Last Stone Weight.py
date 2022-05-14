import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 读题后第一想法：主要考察heap sort

        # 解题方法：搭建一个max heap然后每次取出两个最大的元素相减，得到的值再放回heap中，循环至只有一个元素，输出
        # 因为heapq只能搭建 min heap 所以将每个元素 *-1 最后再输出其正数值
        negative = [-x for x in stones]
        heapq.heapify(negative)
        while len(negative) >= 2:
            smash = heapq.heappop(negative) - heapq.heappop(negative)
            heapq.heappush(negative, smash)
        return heapq.heappop(negative) * -1
    # Time: 93%
    # Space: 100%


# 05-13-2022
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq.heapify()生成的min heap，min heap没有直接搜索最大元素的方法
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
    
    """
    while循环中的巧妙之处：
    1. 第一个heappop的元素必定 <= 第二个，所以无需判断大小或者获取绝对值
    2. 两者相减答案一定是负数或者0
    3. 如果是0，作为最大的元素，必定会被加入到heapq的最后面
    4. 每次循环len(h)必定会-1，所以即使最后heapq中出现多个0，while循环也会在一定阶段停止
    5. 停止时的最小元素则为剩余值
    """
