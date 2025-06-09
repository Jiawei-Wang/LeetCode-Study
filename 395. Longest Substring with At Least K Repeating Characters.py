# sliding window
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        str_arr = list(s) # turn string into list first
        result = 0 # global maximum answer
        
        # find number of unique chars
        def getMaxUniqueLetters(s: str) -> int:
            return len(set(s))
        max_unique = getMaxUniqueLetters(s)

        # we don't know how many unique chars will result in longest substring
        # so we try every number of unique chars 
        for curr_unique in range(1, max_unique + 1):
            count_map = [0] * 26
            window_start = 0
            window_end = 0
            unique = 0 # number of unique chars in the window
            count_at_least_k = 0 # number of unique chars in the window having at least k times

            while window_end < len(str_arr):
                # we use unique value to decide how to move current window
                if unique <= curr_unique: # if we can still add new element
                    idx = ord(str_arr[window_end]) - ord('a')
                    if count_map[idx] == 0:
                        unique += 1
                    count_map[idx] += 1
                    if count_map[idx] == k:
                        count_at_least_k += 1
                    window_end += 1
                else: # if we can no longer add more element
                    idx = ord(str_arr[window_start]) - ord('a')
                    if count_map[idx] == k:
                        count_at_least_k -= 1
                    count_map[idx] -= 1
                    if count_map[idx] == 0:
                        unique -= 1
                    window_start += 1

                # if current window satisfies requirements
                if unique == curr_unique and unique == count_at_least_k:
                    result = max(result, window_end - window_start)

        return result