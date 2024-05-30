"""
MicroSoft 2024 onsite

Input:
array, a list of integers
n, an integer representing how many elements we want to pick from array
Output: the biggest sum we can get from picking n elements from array 
where no 2 elements are adjecent to each other

example: array = [1, 4, 6, 2], n = 2
return 7
"""
def max_sum_no_adjacent(array, n):
    if n == 0 or len(array) < n:
        return 0
    
    dp = [[0] * (len(array) + 1) for _ in range(n + 1)] 
    # dp[k][i]: maximum sum for picking k elements from array[0:i]
    
    for k in range(1, n + 1):
        for i in range(1, len(array) + 1):
            if i == 1:
                dp[k][i] = array[0]
            else:
                dp[k][i] = max(dp[k][i-1], (dp[k-1][i-2] + array[i-1]))
    
    return dp[n][len(array)]


array = [1, 4, 6, 2]
n = 2
print(max_sum_no_adjacent(array, n))  # Output: 7