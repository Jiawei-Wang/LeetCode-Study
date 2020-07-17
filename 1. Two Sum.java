// solution 1: double loop
// Time: n^2
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // 两层循环
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    // https://stackoverflow.com/questions/1200621/how-do-i-declare-and-initialize-an-array-in-java
                    return new int[] {i, j};
                }
            }
        }
        // https://www.w3schools.com/java/ref_keyword_throw.asp
        throw new IllegalArgumentException("No two sum solution");
    }
}


// solution 2: hashing，两次遍历，第一次创建hashmap，第二次对每个元素进行查询
// Time: n，但是需要额外空间存储hashmap，复杂度为n
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // 创建hashmap并放入数据
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            // put(key, value)
            map.put(nums[i], i);
        }
        // 遍历查询
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            // HashMap.containsKey(): true/false
            // HashMap.get(): index
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[] { i, map.get(complement) };
            }
        }
    throw new IllegalArgumentException("No two sum solution");
    }
}
