// solution 1: 暴力解，两层循环
// Time: n^2

class Solution {
    public int numIdenticalPairs(int[] nums) {
        // ans变量记录总数
        // 如何声明新的变量：https://www.geeksforgeeks.org/variables-in-java/
        int ans = 0;

        // n变量记录nums长度
        // 如何获得array和string的长度：https://www.geeksforgeeks.org/length-vs-length-java/
        int n = nums.length;

        // 两层循环
        // For loop: https://www.w3schools.com/java/java_for_loop.asp
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                // if statement: https://www.w3schools.com/java/java_conditions.asp
                // array and arraylist: https://www.javatpoint.com/array-vs-arraylist-in-java
                // get element by index: https://www.w3schools.com/java/java_arraylist.asp
                if (nums[i] == nums[j]) {
                    ans += 1;
                }
            }
        }

        // 返回ans
        // return in java: https://www.w3schools.com/java/ref_keyword_return.asp
        return ans;
    }
}


// solution2: hashmap，遍历数组，在每个位置上时寻找已经出现同值的次数
// Time: n
class Solution {
    public int numIdenticalPairs(int[] nums) {
        // map是interface，hashmap是map的implementation
        Map<Integer, Integer> map = new HashMap();
        int count = 0;
        // for each loop
        for (int num : nums) {
            // HashMap getOrDefault(key, defaultValue) metho: https://www.geeksforgeeks.org/hashmap-getordefaultkey-defaultvalue-method-in-java-with-examples/
            // count += 当前这个num（key）在map中已经出现的次数（value）
            count += map.getOrDefault(num, 0);
            // 如果没有value，放入0+1，如果已有value，+1
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        return count;
    }
}


// solution 3: sorting
// Time: nlogn
class Solution {
    public int numIdenticalPairs(int[] nums) {
        // https://www.geeksforgeeks.org/arrays-sort-in-java-with-examples/
        Arrays.sort(nums);

        int count = 0;
        int i = 0;

        // 从第二个元素开始遍历数组
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] == nums[i])
                // 找出下标为j的这个元素前面和它相同的元素的个数
                count += j - i;
            // 如果不相同则将i设置为该新的元素
            else i = j;
        }
        return count;
    }
}
