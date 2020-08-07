class Solution {
    public int[] constructRectangle(int area) {
        // 获得面积的平方根
        // 从平方根开始向下取整，如果能被整除，则输出 int pair
        for (int l = (int)Math.sqrt(area); l <= area; l++) {
            if (area % l == 0 && l >= (area/l)) {
                return new int[]{l,area/l};
            }
        }
        return new int[]{area,1};
    }
}
