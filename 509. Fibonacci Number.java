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
