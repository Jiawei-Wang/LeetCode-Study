// Lucid OA 2020 Oct
/*
原题结构(in Python):
1. 定义一个函数: def minMoves(maze, x, y), 输入2d list和终点坐标, 返回最少步数
2. 主函数: 1) 读取文件
          2) 获得文件中的输入: row, col, maze(2d list), x, y
          3) 调用minMoves获得return值
          4) 将该值写入文件
3. 主函数已经写好, 只需要写出minMoves的主体即可
*/

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class mazeNavigationsWithCoins {
    int[][][] dist;
    int[][] dp;
    List<int[]> coins; // 2d list with all available coins on map
    int R; // maze rows
    int C; // maze columns
    int allOnes, numCoins; // numCoins: number of all coins
    int MAXDIST = 1000 * 1000;


    boolean isInRange(int r, int c) {
        return r >= 0 && r < R && c >= 0 && c < C;
    }

    // Put every coin on the map into 2d list: coins
    void extractCoins(int[][] arr, List<int[]> coins) { // arr: 2d maze; coins: 2d list initialized with [[0, 0]]
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (arr[r][c] == 2) {
                    int[] point = {r, c};
                    coins.add(point);
                }
            }
        }
    }


    void setDistances(int[][] arr, int coin) {

        // set everything to MAXDIST
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) dist[r][c][coin] = MAXDIST;
        }

        boolean[][] visited = new boolean[R][C];
        Queue<int[]> q = new LinkedList<>();
        int[] startPoint = coins.get(coin);
        q.add(startPoint);
        visited[startPoint[0]][startPoint[1]] = true;
        dist[startPoint[0]][startPoint[1]][coin] = 0;


        int[] dr = {0, -1, 0, 1};
        int[] dc = {-1, 0, 1, 0};

        while (!q.isEmpty()) {
            int[] point = q.poll();
            int oldR = point[0];
            int oldC = point[1];
//            System.out.println("oldR= " + oldR + " oldC= " + oldC + " coin= " + coin + " dist[oldR][oldC][coin]= " + dist[oldR][oldC][coin]);
            for (int k = 0; k < 4; k++) {
                int newR = oldR + dr[k];
                int newC = oldC + dc[k];
                if (isInRange(newR, newC) && !visited[newR][newC] && arr[newR][newC] != 1) {
                    int[] newPoint = {newR, newC};
                    visited[newR][newC] = true;
                    dist[newR][newC][coin] = dist[oldR][oldC][coin] + 1;
                    q.add(newPoint);

                }

            }

        }

    }

    int getMinDist(int coin, int seq, int Ra, int Ca) {
        // seq - keeps track of the nodes/coins included in the "spanning tree"
        // 0 means that coin has not been considered, and isn't in the spanning tree
        // 1 means it has been considered

        if (seq == allOnes) return dist[Ra][Ca][coin];
        if (dp[coin][seq] != -1) return dp[coin][seq];

        int res = Integer.MAX_VALUE;
        for (int i = 0; i < numCoins; i++) {
            // (seq & (1 << i)) == 0 means i hasn't been included
            // in the current "spanning tree"
            if ((seq & (1 << i)) == 0) {
                int newSeq = seq | (1 << i);
                int[] pos = coins.get(i);
                res = Math.min(res, getMinDist(i, newSeq, Ra, Ca) + dist[pos[0]][pos[1]][coin]);

            }
        }

        dp[coin][seq] = res;
//        System.out.println("coin = " + coin + " seq = " + " res = " + res);
        return res;

    }

    int minMoves1(int[][] arr, int Ra, int Ca) { // arr: 2d maze; [Ra, Ca]: Target position
        R = arr.length; // R: maze rows
        C = arr[0].length; // C: maze columns
        int[] startPoint = {0, 0};

        // initialise coins
        coins = new ArrayList<>();
        coins.add(startPoint);
        extractCoins(arr, coins); // arr: 2d maze; coins: 2d list initialized with [[0, 0]] 
        numCoins = coins.size();
        allOnes = (1 << numCoins) - 1; // 1 * 2^numCoins - 1
//        System.out.println("allOnes = " + allOnes);

        // initialise dp
        // maximum no. of coins = 10, max number of 'trees' = 2**10
        int dpR = numCoins;
        int dpC = allOnes + 1;
        dp = new int[dpR][dpC];
        for (int i = 0; i < dpR; i++) {
            for (int j = 0; j < dpC; j++) dp[i][j] = -1;
        }


        // get distance of each square from each coin
        dist = new int[R][C][numCoins];
        for (int i = 0; i < numCoins; i++) setDistances(arr, i);

        // solve recursively!
        int ans = getMinDist(0, 1, Ra, Ca);
        return ans >= MAXDIST ? -1 : ans;

    }


    public static void main(String[] args) {
        mazeNavigationsWithCoins soln = new mazeNavigationsWithCoins();

        // output should be 4
        int[][] arr = {{0, 2, 1}, {1, 2, 0}, {1, 0, 0}};
        int x = 2;
        int y = 2;
        System.out.println(soln.minMoves1(arr, x, y));

        // output should be 2
        arr = new int[][]{{0, 2, 0}, {0, 0, 1}, {1, 1, 1}};
        x = 1;
        y = 1;
        System.out.println(soln.minMoves1(arr, x, y));

        // output should be -1
        arr = new int[][]{{0, 1, 0}, {1, 0, 1}, {0, 2, 2}};
        x = 1;
        y = 1;
        System.out.println(soln.minMoves1(arr, x, y));

        // output should be 5
        arr = new int[][]{{0, 2, 0}, {1, 1, 2}, {1, 0, 0}};
        x = 2;
        y = 1;
        System.out.println(soln.minMoves1(arr, x, y));

        arr = new int[][]{{0, 2, 0}, {1, 2, 1}, {1, 1, 1}};
        x = 0;
        y = 2;
        System.out.println(soln.minMoves1(arr, x, y));
    }
}