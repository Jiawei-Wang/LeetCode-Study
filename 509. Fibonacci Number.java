// 学习 iteration and recursion：前者是循环，后者是反复call itself

// iteration
class Solution {
    public int fib(int N) {
        // 首先corner case
        if (N == 0) { return 0; }
        if (N == 1) { return 1; }
        // 其次进行循环
        int first = 0;
        int second = 1;
        int ans = 0;
        for (int i = 2; i <= N; i++) {
            ans = first + second;
            first = second;
            second = ans;
        }
        // 最后输出
        return ans;
    }
}

// recursion
class Solution {
    public int fib(int N) {
        if (N == 0) {return 0;}
        if (N == 1) {return 1;}
        return fib(N-1)+fib(N-2);
    }
}


// Aug 8 2020
// 使用此题作为DP的学习材料

// pure recursion
// 逻辑：定一个base case和一个recursive form，无需使用任何额外空间，使用stack的形式反复call function
class Solution {
    public int fib(int N) {
        // base case
        if (N ==0) return 0;
        if (N ==1) return 1;
        // recursion
        return fib(N-1)+fib(N-2);
    }
}
