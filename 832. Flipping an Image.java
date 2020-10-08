// 做题思路：
// 1. 读题：题目是什么意思，给了什么输入，要求什么输出
// 2. 算法：获得一个初步的模糊解法
// 3. 优化：怎么样获得更佳算法，以及trade off
// 4. corner case
// 5. 选用什么数据结构
// 6. coding


// 读题：输入一个2d array，输出一个2d array
// 算法：1.每个row进行翻转，2.每个数字取反
// 优化：1.直接在原array上进行操作节约内存，2.想办法高效翻转

class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        // 遍历每个row
        for (int i = 0; i < A.length; i ++) {
            // 进行翻转: 每两个元素互相交换；然后取反
            for (int j = 0; j < (A[0].length+1)/2; j ++) { // 注意这里使用(length+1)/2来确保遍历半个数组
                // ^1的作用：XOR，如果该数为1，则返回0，若为0，则返回1
                int temp = A[i][j]^1;
                A[i][j] = A[i][A[0].length-1-j]^1;
                A[i][A[0].length-1-j] = temp;
            }
        }
        // 输出
        return A;
    }
}
