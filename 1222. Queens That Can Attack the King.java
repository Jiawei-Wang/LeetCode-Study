// 读题后的想法：寻找从国王出发的8个方向上，每个方向的第一个皇后（如果存在）
class Solution {
    public static String COLON = ":";
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        List<List<Integer>> rslt = new ArrayList<>();
        Set<String> qset = new HashSet<>();

        // 将2d array queens中的所有元素，以string的形式加入set qset中
        for(int[] qpos : queens){
            String str = qpos[0] + COLON + qpos[1];
            qset.add(str);
        }


        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                for(int k = 1; k < 8; k++){
                    int xpos = king[0] + i*k;
                    int ypos = king[1] + j*k;
                    String ts = xpos + COLON + ypos;
                    // 查询string是否在set中
                    if (qset.contains(ts)){
                        rslt.add(Arrays.asList(xpos,ypos));
                        break;
                    }
                }
            }
        }
        return rslt;
    }
}
