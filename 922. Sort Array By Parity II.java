// 解法1：创建一个新的list，把偶数放在偶数位置，奇数放在奇数位置
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int[] ans = new int[A.length];
        int even = 0;
        int odd = 1;
        for (int i = 0; i < A.length; i++) {
            if (A[i] % 2 == 0) {
                ans[even] = A[i];
                even += 2;
            } else {
                ans[odd] = A[i];
                odd += 2;
            }
        }
        return ans;
    }
}


// 解法2：in place
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int j = 1;
        for (int i = 0; i < A.length; i += 2)
            if (A[i] % 2 == 1) {
                while (A[j] % 2 == 1)
                    j += 2;
                // Swap A[i] and A[j]
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        return A;
    }
}

/*
对于解法2的理解：
i 代表全部偶数位置
j 代表全部奇数位置
如果 i 上出现奇数，在 j 中找到一个偶数，然后两者交换
*/
