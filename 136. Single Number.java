class Solution {
    public int singleNumber(int[] nums) {
        // 关于XOR的阅读：https://stackoverflow.com/questions/1991380/what-does-the-operator-do-in-java
        // 对于本题：a^a^b^b^c^c^d^d^x = 0^0^0^0^x = x
        int ans =0;
        // 注意length后没有括号
        int len = nums.length;
        for(int i=0;i!=len;i++)
            ans ^= nums[i];
        return ans;
    }

    // method using set
    TODO


}
