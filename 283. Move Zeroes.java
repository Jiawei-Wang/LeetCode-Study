// 解法1：使用一个新array，对它进行操作，最后用它覆盖nums
class Solution {
    public void moveZeroes(int[] nums) {
        // 创建一个新array
        int[] newArray = new int[nums.length];
        // 遍历nums，如果元素非0，放进新array，同时统计0的总数
        int totalZero = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                totalZero += 1;
            } else {
                newArray[i-totalZero] = nums[i];
            }
        }
        // 把新array的尾部填充满0
        for (int j = nums.length-totalZero; j < nums.length; j ++) {
            newArray[j] = 0;
        }
        // 把新array的值给nums
        for (int i = 0; i < nums.length; i++) {
            nums[i] = newArray[i];
        }
        /*
        以下是错误方法，因为指针虽然变了但本体并未改变：

        // 让nums的指针指向新array
        nums = newArray;

        */
    }
}
