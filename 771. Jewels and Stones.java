class Solution {
    public int numJewelsInStones(String J, String S) {
        int res = 0;
        // 关于interface和class:
        // https://stackoverflow.com/questions/3715209/when-defining-set-set-new-hashset-is-set-an-instance-of-interface-or-clas
        Set setJ = new HashSet();
        // 如何将string变为char list，如何遍历每个元素
        for (char j: J.toCharArray())
            setJ.add(j);
        for (char s: S.toCharArray())
            // 如何查找元素是否在set内：
            if (setJ.contains(s)) res++;
        return res;
    }
}
