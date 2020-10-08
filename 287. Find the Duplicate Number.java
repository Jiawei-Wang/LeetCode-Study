// 解法1：先sort，然后遍历找出重复元素
// Time: nlogn
// Space: 1
class Solution {
    public int findDuplicate(int[] nums) {
        // sort
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1]) {
                return nums[i];
            }
        }

        return -1;
    }
}


// 解法2: 使用hashset
// Time: n
// Space: n
class Solution {
    public int findDuplicate(int[] nums) {
        // new hashset
        Set<Integer> seen = new HashSet<Integer>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return num;
            }
            seen.add(num);
        }

        return -1;
    }
}


// 解法3：double loop
// Time: n^2
// Space: 1
class Solution {
    public int findDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j ++){
                if (nums[i] == nums[j]){
                    return nums[i];
                }
            }
        }
        return -1;
    }
}


// 解法4：对数值进行二分查找而非index: https://zhuanlan.zhihu.com/p/76698113
// Time：nlogn
// Space: 1
class Solution {
    public int findDuplicate(int[] nums) {
        // 一共有 n 个位置给数字 1 到 n-1
        int n = nums.length;
        int left = 1, right = n - 1; // 这里是数值而非索引

        while (left < right) {
            int mid = left + (right - left) / 2; // 防止溢出的方式
            int counter = 0;
            for(int i = 0; i < n; ++i) {
                if(nums[i] <= mid) counter++;
            }
            if(counter > mid) right = mid;
            else left = mid + 1;
        }
        return left;
    }
}


// 解法5：Floyd's Tortoise and Hare (Cycle Detection)
// 将每个元素的值视为指向下一个元素的index，就可以获得一个环，而环的起点就是重复的元素
// Time: n
// Space: 1
class Solution {
    public int findDuplicate(int[] nums) {
        // phase 1:
        // Find the intersection point of the two runners.
        int tortoise = nums[0];
        int hare = nums[0];
        // do while可以保证至少做一次，所以第一次两者都从起点出发就可以省去判断阶段
        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while (tortoise != hare);
        // 结束时两者拥有相同的值

        // phase 2:
        // Find the "entrance" to the cycle.
        // 兔子从两者phase1的交点出发，乌龟从起点出发，两者速度相同，一定会在环的起始点相遇
        tortoise = nums[0];
        while (tortoise != hare) {
            tortoise = nums[tortoise];
            hare = nums[hare];
        }

        return hare;
    }
}
