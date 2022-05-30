"""
逻辑很清晰，但是没过test case [1,3,4,6]，应该返回True但是返回了False，需要再研究一下
"""
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # 2张卡片有5种可能计算结果
        def compute(a, b):
            res = set([a+b, a-b, a*b])
            if a:
                res.add(b/a)
            if b:
                res.add(a/b)
            return res
        
        def dfs(list): # list是（当前计算结果）+（等待被计算的卡片）的集合，最初是（0个计算结果）+（4个待计算卡片）
            
            # 如果4张卡片都被计算完了，那么就只剩一个计算结果，检查其是否为24
            if len(list) == 1:
                if abs(list[0] - 24.0) < 0.001:
                    return True
                return False
            
            # 对于所有的两两数字组合
            for i in range(len(list)):
                for j in range(i+1, len(list)):
                    # 每个组合有5种计算结果，遍历所有结果
                    for c in compute(list[i], list[j]):
                        nextRound = []
                        nextRound.append(c)
                        # 对于每种结果，继续添加卡片来进行下一轮计算
                        for k in range(len(list)):
                            if k == j or k == i:
                                continue
                            nextRound.append(list[k])
                        if dfs(nextRound):
                            return True
            return False
        
        # 将所有数字转为浮点数然后dfs
        list = []
        for i in cards:
            list.append(float(i))
        return dfs(list)