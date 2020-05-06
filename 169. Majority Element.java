class Solution {
    public int majorityElement(int[] nums) {
        // sort list的语法
        Arrays.sort(nums);
        // 1.获得list长度，2.整除用一个斜杠，3.使用index获得元素
        return nums[nums.length/2];
    }
}
