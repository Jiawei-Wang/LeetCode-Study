# 理解题意：有一个list的汽车，每个车有position和speed，当它追上前面的车时车速会保持和前车一致，直到终点
# 找到到达终点时一共有多少个车队（1辆车也算1个车队）
# 纸上画例子时发现的：
#    任何时间时后车追赶上前车（即此时间点时后车position小于前车，但下一个时间点时后车position>=前车），
#    后车都会被直接取消掉（即二者变成一个车队，以前车速度前进）
# 同时题目规定：恰好在终点追赶上前车的后车，仍被单独考虑为一个车队

# 先暴力解：模拟每一步
# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         ans = 0 # 一共有多少个车队
#         # 最后一辆车还没到终点前都需要模拟
#         while min(position) < target:
#             # 一共有5种情况需要考虑：
#             # 1. 前后车没相遇
#             # 2. 后车正好追上前车
#             # 3. 后车超过前车
#             # 4. 后车正好在终点追上前车
#             # 5. 任何一辆车到达终点或者超过终点
#             for car in position:
#                 car += speed
#             for i in range(len(position)-1,-1,-1):
#                 if position[i] > target:
                    
#                 elif position[i] == target:
#                 else:

# 模拟的问题在于有过多的case需要讨论
# 换个视角，将每辆车视为一个方程 y = ax + b，则起始位置为b，速度为a
# 那么当两条直线在终点y = target前相交时，斜率更大的直线就被抹除
# 由此衍生：如果后面一辆车到达终点的时间 <= 前面车，则二者融合
# 算法：从最前面的车（离终点最近）开始，逐个检查是否会被融合
# time O(nlogn): decided by sorting 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        time = 0
        count = 0
        for p, s in sorted(pair)[::-1]:
            current = (target - p)/s
            if current <= time:
                continue
            count += 1
            time = current
        return count
