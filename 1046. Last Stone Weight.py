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
