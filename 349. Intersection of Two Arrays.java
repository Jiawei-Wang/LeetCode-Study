// 解法1：two sets
// 思路：使用两个list进行遍历，复杂度为 n^2，但是使用set可以使单次查询时间减为 1
class Solution {
    // helper function
    public int[] set_intersection(HashSet<Integer> set1, HashSet<Integer> set2) {
        int [] output = new int[set1.size()];
        int idx = 0;
        for (Integer s : set1)
        // 使用 contains() 来查询元素是否存在
        if (set2.contains(s)) output[idx++] = s;
        // 将output进行复制，然后裁剪成 length = idx 的长度
        return Arrays.copyOf(output, idx);
    }

    // main function
    public int[] intersection(int[] nums1, int[] nums2) {
        // 如何创建一个新的hashset
        HashSet<Integer> set1 = new HashSet<Integer>();
        // 如何copy元素
        for (Integer n : nums1) set1.add(n);
        HashSet<Integer> set2 = new HashSet<Integer>();
        for (Integer n : nums2) set2.add(n);
        // 使用 size() 来查询hashset长度
        if (set1.size() < set2.size()) return set_intersection(set1, set2);
        else return set_intersection(set2, set1);
    }
}


// 解法2：Built-in Set Intersection
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        HashSet<Integer> set1 = new HashSet<Integer>();
        for (Integer n : nums1) set1.add(n);
        HashSet<Integer> set2 = new HashSet<Integer>();
        for (Integer n : nums2) set2.add(n);

        // 将 set1 中在 set2 中出现的元素保留，其余丢弃
        set1.retainAll(set2);

        // set转换为list
        int [] output = new int[set1.size()];
        int idx = 0;
        for (int s : set1) output[idx++] = s;
        return output;
    }
}
