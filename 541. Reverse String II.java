// String在java中是一种不可修改的数据结构，所以必须借助额外的空间

// 解法1：转换成 char array然后进行操作
class Solution {
    public String reverseStr(String s, int k) {
        // 首先是转换成array
        char[] a = s.toCharArray();
        // 找到每 2k 长度的子字符串片段
        for (int start = 0; start < a.length; start += 2 * k) {
            // 如果是最后一个片段，则 j 为末尾元素的下标
            int i = start, j = Math.min(start + k - 1, a.length - 1);
            while (i < j) {
                char tmp = a[i];
                a[i++] = a[j];
                a[j--] = tmp;
            }
        }
        // 最后将array转换回String
        return new String(a);
    }
}
