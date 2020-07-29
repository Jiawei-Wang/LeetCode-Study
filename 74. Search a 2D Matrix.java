// binary search：将2d list视为1d来对待
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        // corner case
        if (matrix == null || matrix.length == 0) {
            return false;
        }

        int start = 0; // 左上角元素在1d list中的index
        int rows = matrix.length, cols = matrix[0].length;
        int end = rows * cols - 1; // 右下角元素在1d list中的index

        while (start <= end) {
            int mid = (start + end) / 2;
            // 学习这种将1d index放回2d list中的方法
            if (matrix[mid / cols][mid % cols] == target) {
                return true;
            }
            if (matrix[mid / cols][mid % cols] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return false;
    }
}
