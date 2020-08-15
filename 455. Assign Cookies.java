// 读题感想：对于g中的每个元素，查找s中 >= 它的最小元素，如果存在，count+1，s中删除这个元素
// 改进：先sort两个array，然后遍历s，如果当前元素大于等于g中的元素，g走到下一个元素
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int i = 0;
        for(int j=0; i<g.length && j<s.length; j++) {
            if(g[i]<=s[j]) i++;
        }
        // 虽然i是下标，但是因为它指向的是最后一个符合要求的元素的下一个元素，所以值正好等于符合要求的元素的总和
        return i;
    }
}
