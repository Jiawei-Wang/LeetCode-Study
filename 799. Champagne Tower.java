// 解法1：Simulation
// 逻辑如下：当一个杯子接受 n 的酒时，它下方两个各收到 (n-1)/2 的酒
// 这个解法逐行计算每个杯子总共接受了多少酒，总共向下方倒出多少酒
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        // double中每个位置存储的是倒进该位置的酒的总量
        double[][] A = new double[102][102];
        A[0][0] = (double) poured;
        for (int r = 0; r <= query_row; ++r) {
            for (int c = 0; c <= r; ++c) {
                // q 存储的是经过 A[r][c]向下方两个方向每边倒出的酒
                double q = (A[r][c] - 1.0) / 2.0;
                if (q > 0) {
                    A[r+1][c] += q;
                    A[r+1][c+1] += q;
                }
            }
        }

        return Math.min(1, A[query_row][query_glass]);
    }
}


// DP
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        // 使用1d array的理由是：只需要不停更新array直到需要搜索的对应行即可，前面行的信息不需要保留
        double[] res = new double[query_row + 2];
        res[0] = poured;

        // 从第1行（2个杯子的那一行）开始
        for (int row = 1; row <= query_row; row++) {
            // 第 n 行有 n+1 个杯子，正好是从0到n
            for (int i = row; i >= 0; i--) {
                // 此时的res[i+1]是res[i]右下角的杯子
                // 注意这句语法：1.先更新了res[i]，2.然后更新了res[i+1]
                // res[i+1] default = 0
                res[i + 1] += res[i] = Math.max(0.0, (res[i] - 1) / 2);
            }
        }

        return Math.min(res[query_glass], 1.0);
    }
}
