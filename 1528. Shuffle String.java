// 解法1：list
class Solution {
    public String restoreString(String s, int[] indices) {
        // 创建一个新的char list
        char[] a = new char[s.length()];
        // 遍历indices，将s中对应元素放入新的位置
        for (int i = 0; i < s.length(); i++) {
            a[indices[i]] =  s.charAt(i);
        }
        // 将list变成string，输出新的string
        return new String(a);
    }
}
/*
1. 没有必要使用 ArrayList，普通list就可以
2. 使用 charAt() 获得string中的某个char
2. 使用 String.valueOf() 或者 new String() 将变量转换为string
*/


// 解法2：Cyclic Sort
class Solution {
    public String restoreString(String s, int[] indices) {
        // 将 s 转换为一个char list
        char[] a = new char[s.length()];
        for (int i = 0; i < s.length(); i++) {
            a[i] = s.charAt(i);
        }
        // cyclic sort
        for (int i = 0; i < indices.length; i++) {
            while (indices[i] != i) {
                char temp = a[i];
                a[i] = a[indices[i]];
                a[indices[i]] = temp;

                int Temp = indices[i];
                indices[i] = indices[indices[i]];
                indices[indices[i]] = Temp;
            }
        }
        return new String(a);
    }
}
