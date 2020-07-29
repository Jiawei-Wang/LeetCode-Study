class Solution {
    // 保存的是26个字母在order中的顺序
    int[] mapping = new int[26];

    // main function
    public boolean isAlienSorted(String[] words, String order) {
        for (int i = 0; i < order.length(); i++)
            // 举例：order中第0个元素是'z'（表示'z'是字典中最前面的元素）
            // 那么mapping中第25个元素（也就是正常字典中'z'的位置）的值就是0
            mapping[order.charAt(i) - 'a'] = i;

        for (int i = 1; i < words.length; i++)
            if (bigger(words[i - 1], words[i]))
                return false;
        return true;
    }

    // helper function
    // 这个方程需要返回s1是否在order中大于s2（即s1的顺序是否在s2之后）
    public boolean bigger(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        // 遍历string，遇到同位置不相同的字符时，返回两个字符对应顺序的比较
        for (int i = 0; i < n && i < m; ++i)
            if (s1.charAt(i) != s2.charAt(i))
                // 如果为true，意思是s1该位置上的字符应该在s2对应的字符之后
                return mapping[s1.charAt(i) - 'a'] > mapping[s2.charAt(i) - 'a'];
        // 如果遍历完依旧没有返回值，返回两个string长度对比
        return n > m;
    }
}
