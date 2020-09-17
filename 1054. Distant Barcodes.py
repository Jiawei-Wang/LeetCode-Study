import collections

# 解法1
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # 初始化一个array
        i, n = 0, len(barcodes) # i是下标, n是barcodes长度
        res = [0] * n
        
        # 将barcodes中所有元素的出现次数记录下来, 然后对于出现次数最多的那个元素:
        # collections.Counter(barcodes) 返回一个counter, 里面是每个元素和它的出现次数
        # counter.most_common() 返回一个array, 里面是按照出现次数从多到少排列的多个tuple = (元素, 出现次数)
        for k, v in collections.Counter(barcodes).most_common():
            
            # 从头开始, 每隔一个位置放入一个, 其他的元素也隔一个位置放入一个, 奇偶分开遍历
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n: i = 1
                    
        return res