class Solution {
    // 同python版思路，遍历元素，每三个元素之间两两的斜率均相同
    // int[][] 代表2d list
    public boolean checkStraightLine(int[][] coordinates) {
        // 这种创建变量的表达方式
        int x0 = coordinates[0][0], y0 = coordinates[0][1],
            x1 = coordinates[1][0], y1 = coordinates[1][1];
        int dx = x1 - x0, dy = y1 - y0;
        for (int[] co : coordinates) {
            int x = co[0], y = co[1];
            if (dx * (y - y1) != dy * (x - x1))
                return false;
        }
        
        return true;
    }
}
