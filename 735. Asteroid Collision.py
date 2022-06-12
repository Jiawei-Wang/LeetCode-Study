# asteroids是一个1d list，其中有若干整数（正数表示彗星向右走，负数表示向左走）
# 两个彗星相遇绝对值较小者被摧毁，两者相同则都被摧毁
# 返回所有相撞发生完成后的情况

'''
读题感想：
左侧开头部分连续的负数都会被保留，右侧末尾部分连续的正数都会被保留
（因为开头向左飞的彗星和末尾向右飞的永远不会遇到别的彗星）
左侧第一个正数和右侧第一个负数，两者的中间部分是需要考虑的
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            # stack中放入正数时，无论当前顶部元素是正是负，都不会碰撞
            # stack中放入负数时，必须当前顶部元素为正数，才会碰撞
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new: # 如果向左的彗星比向右的大，则一直pop到出现负数或者不小于它的正数为止
                    ans.pop()
                    continue # 跳过break，进入下一次循环接着找
                elif ans[-1] == -new: # 如果正数一样大则pop掉正数
                    ans.pop()
                break # 正数和它一样大则pop然后离开循环，正数比它大则直接离开循环，什么也不做
            else:
                ans.append(new) # 不会碰撞的情况下则直接将它加入当前stack
        return ans