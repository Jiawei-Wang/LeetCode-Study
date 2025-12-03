# 在只有0和1的list中找到0和1数量相等的最长sublist的长度

# 使用count记录每一步时的0和1数量差值, 如果nums[i]和nums[j]的count相同，说明这两点间0和1数量相同
# 所以对于同一个count值而言，其对应的最长长度是第一次和最后一次出现此值对应的sublist
# 所以可以创建一个list，index = nums的index，value = count (这样做还需要再遍历list来找出value相同的两个元素index最大差值）
# 优化：
# 已知count的范围是[-n,+n]，所以我们如果使用一个长度为（2n+1）的list，就可以将两者对调：
# list的index = count，value = 第一次出现此count时在nums中所在的位置
# 逻辑：第一次获得新的count值，记录在nums中的位置，第二次以及以后再获得此count值，直接减法获得length
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [float('-inf')] * (2*n+1) # index = count, value = 第一次出现该count时在nums中的位置
        arr[n] = -1 # 长度 = 最后一个元素下标 - 第一个元素下标 + 1，假设index = 5时count = 0，那么长度为6，所以count = 0的第一个index = -1
        cnt = 0
        maxLen = 0
        for i in range(n):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt -= 1
            
            if arr[n+cnt] != float('-inf'):
                maxLen = max(maxLen, i - arr[n+cnt])
            else:
                arr[n+cnt] = i 
                
        return maxLen


# 对于上一解的优化：使用dictionary代替list来节约空间，其余相同
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        arr = dict()
        arr[n] = -1
        cnt = 0
        maxLen = 0
        for i in range(n):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt -= 1
            
            if n+cnt in arr:
                maxLen = max(maxLen, i-arr[n+cnt])
            else:
                arr[n+cnt] = i
        return maxLen


# 2025
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0 # how many more 1s than 0s
        max_length = 0
        table = {0: -1}
        
        for index, num in enumerate(nums):  
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index

        return max_length

        