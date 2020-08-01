// 参考答案
class Solution {
    public int compress(char[] chars) {
        // indexAns是用于修改原array的指针，index是用于保存遍历时的下标
        int indexAns = 0, index = 0;

        while(index < chars.length){
            char currentChar = chars[index];
            int count = 0;
            // 这个循环的意思是：只要字符相同就一直遍历，记录其数量，同时让下标最终停在第一个不同的字符上
            while(index < chars.length && chars[index] == currentChar){
                index++;
                count++;
            }
            // 先把刚才循环中的字符记录下来，然后让指针向后挪一位
            chars[indexAns++] = currentChar;
            if(count != 1) {
                // 这句话的意思是把count这个整数，的每一位变成一个字符
                for(char c : Integer.toString(count).toCharArray())
                    chars[indexAns++] = c;
            }
        }
        return indexAns;
    }
}

/*
对于答案的理解：双指针。第一个指针用于修改array，第二用于遍历array
一、先使用index:
1. 记录下当前所在的位置的字符
2. 一直向后遍历直到找到不同的字符，在此过程中记录字符出现次数和新字符的下标
二、然后使用indexAns:
3. 把array中对应位置修改成字符和它出现次数
三、最后使用index开始继续遍历
*/


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
