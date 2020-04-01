class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        // 按照此题Python答案的逻辑改写，依旧是根据数字在Tree中唯一的固定位置找到parent node并挨个输出
        // 重点是锻炼Java语法

        // 创建list并将label放入
        List<Integer> ans = new ArrayList<>();
        ans.add(0, label);

        // 找出label在Tree中的位置
        int row = 1;
        int column;
        while (label > (int)Math.pow(2, row)-1) {
            row += 1;
        }
        if (row % 2 == 1) {
            column = label - (int)Math.pow(2, row-1) + 1;
        } else {
            column = (int)Math.pow(2, row-1) - (label - (int)Math.pow(2, row-1) + 1) + 1;
        }

        // 循环找出每个parent node的值
        int value;
        while (row > 1) {
            row -= 1;
            column = (int)(column + 1)/2;
            if (row % 2 == 1) {
                value = (int)Math.pow(2, row-1) - 1 + column;
            } else {
                value = (int)Math.pow(2, row-1) - 1 + (int)Math.pow(2, row-1) - column + 1;
            }
            ans.add(0, value);
        }
        return ans;
    }
}

/*
1.严格按照数学的逻辑来书写算式，但是
2.算式有很多冗余
3.java语法有很多冗余，但是
4.这个解法在时间和空间复杂度上都打败了100%的人，NICE！
*/
