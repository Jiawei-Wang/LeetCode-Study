// 读题后的想法：将list转换为ordered set然后遍历set即可
// 但是问题在于：set中的元素不存在order

// HashMap
class Solution {
    public int findPairs(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k < 0)   return 0;

        // map保存的是nums中所有的元素和它们的出现次数
        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;
        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        // 下面这句话是遍历map的最佳语法
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (k == 0) {
                //count how many elements in the array that appear more than twice.
                if (entry.getValue() >= 2) {
                    count++;
                }
            } else {
                if (map.containsKey(entry.getKey() + k)) {
                    count++;
                }
            }
        }
        return count;
    }
}
