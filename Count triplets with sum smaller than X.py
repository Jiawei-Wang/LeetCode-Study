# arr中有n个元素，找到所有满足总和<sum的triplets
# for loop + two pointer
# time n^2
class Solution:
    def countTriplets(self, arr, n, sum):
        arr.sort()
        ans = 0
        
        # 因为每个元素都不同，所以不需要像 3Sum 里那样每走一步检查是否和上一个元素相同
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while(j < k):
                if (arr[i]+arr[j]+arr[k] >=sum):
                    k = k-1
                else:
                    ans += (k - j) # 当前总和<sum，所以不需要再去让k往左挪去逐个检查了，直接让j步进，进入下一个循环即可
                    j = j+1
         
        return ans