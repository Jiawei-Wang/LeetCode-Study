/*
以下是个人解法的第一次尝试，没有考虑到一个corner case：某个元素在其他元素出现后再次出现的情况，在这种情况下无法使用
hashmap，所以这个答案是错误的，但是它提供了很多有学习价值的语法

// 题目要求两点：1. in place修改原array；2. 返回修改后array的长度
class Solution {
    public int compress(char[] chars) {
        // 使用一个hashmap将每个字符和它出现次数记录下来
        HashMap<Character, Integer> map = new HashMap<>();
        for (char i : chars) {
            map.put(i, map.getOrDefault(i, 0)+1);
        }

        // 遍历map，将key-value整合成一个string
        String total = "";
        Iterator it = map.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry)it.next();
            char element = (char)pair.getKey();
            int number = (int)pair.getValue();
            if (number > 1) {
                total = total + element + String.valueOf(number);
            } else {
                total = total + element;
            }
            it.remove(); // avoids a ConcurrentModificationException
        }

        // 使用string来修改原array，并裁剪长度
        int i = 0;
        for (char ch: total.toCharArray()) {
            chars[i] = ch;
            i ++;
        }
        chars = Arrays.copyOfRange(chars, 0, total.length());

        return chars.length;
    }
}
*/
