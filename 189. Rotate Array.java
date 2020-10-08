class Solution {
    public void rotate(int[] nums, int k) {
        // 这句话的意思是，如果k大于nums.length，就等于是原地不动外加多余部分移动
        k %= nums.length;
        // 将整个list翻转，然后翻转两个对应部分
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    // 这个method将范围内元素翻转
    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            // java需要使用temp来当作中间变量
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
