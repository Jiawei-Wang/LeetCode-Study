// solution1: liberary
// toLowerCase() method converts a string to lower case letters
class Solution {
    public String toLowerCase(String str) {
        return str.toLowerCase();
    }
}


// solution2
class Solution {
    public String toLowerCase(String str) {
        // 将string转换为array
        char[] a = str.toCharArray();
        // 遍历array
        for (int i = 0; i < a.length; i++)
            // 注意这种判断元素是否为字符的方式
            if ('A' <= a[i] && a[i] <= 'Z')
                a[i] = (char) (a[i] - 'A' + 'a');
        return new String(a);
    }
}


// solution3
class Solution {
     public String toLowerCase(String str) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char c = (char)(str.charAt(i) | (char)(32));
            sb.append(c);
        }
        return sb.toString();
    }
}

/*
解析：
1. String是不可变的
2. 关于stringbuilder: https://www.runoob.com/java/java-stringbuffer.html
3. "|": bitwise OR (还没理解这部分)
*/
