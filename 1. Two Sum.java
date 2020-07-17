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

/*
在python中跑testcase: nums = [3,3], target = 6 时发现两个问题：
1. 如何解决hashmap里每个key只能保存一个value的问题
2. 为什么python中出现了这个testcase跑不过的问题

1. 答：
   这个问题无法解决，java的hashmap和python的dictionary中，每个key都只能存一个value，新的value会替换旧的value，所以nums数组中出现多次的数字，
   只会保留最后一次出现的index。
   其次为什么在java中虽然每个key（元素）只保存了一个value（该元素最后一次出现的index），但这个solution通过了所有的testcase：
   因为首先index相同这个问题只会在以下情况下出现：即当前数字 = 1/2 target且nums中该数字只出现一次，如果出现多次的话就没有此问题，
   因为遍历时找到的是第一次出现的index，而hashmap中保存的是最后一次出现的index，两者不相同。

2. 答：
   因为原代码中遍历查询使用的是 for i in nums 而不是 for i in range(len(nums))，而第一句代码中的 i ，如果查询它的index，python会给出 “i”
   这个值第一次出现时的index，比如 [3,1,3] 中，如果查询每个 i，给出的index为：0，1，0 而非 0，1，2
*/


// solution 3: one pass hashing，遍历所有元素，如果hashmap中有complement，立刻返回，如果没有，将这个元素放入然后前进至下一个元素
// Time: n
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
