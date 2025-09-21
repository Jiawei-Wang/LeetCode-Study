# 最终答案的substring是：找出此substring中最高频的char并替换掉其他的char
# 此char并不一定是整个string中最高频的char，比如：
# s = 'ABABABABABCCCDCCCABABABABAB', K = 1
# 那么显然替换掉D可得最优解


# sliding window
# time 26n, space 26
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 # left pointer
        frequency = {} # freq hashmap
        longest_str_len = 0 # global best answer
        for r in range(len(s)): # move right pointer to each index
            # update freq hashmap first
            if not s[r] in frequency:
                frequency[s[r]] = 0
            frequency[s[r]] += 1
            
            # then update answer
            cells_count = r - l + 1
            if cells_count - max(frequency.values()) <= k: 
                longest_str_len = max(longest_str_len, cells_count)
            else: # else we move left pointer one step
                frequency[s[l]] -= 1 
                if not frequency[s[l]]:
                    frequency.pop(s[l])
                l += 1
                """
                关于为什么每一次循环都让r向前走，但最多只需要 l += 1的解释：
                我们想要的是最长substring，所以如果l和r都前进一步后的substring不符合此长度下的条件，
                则没必要去进一步知道缩减到什么程度时可以符合条件
                """
        
        return longest_str_len
    
    
# time n space 26
# 逻辑：只保留max frequency的元素的最大值，因为 lenth <= k + maxf，所以maxf减小时表示此答案一定非最优解
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res