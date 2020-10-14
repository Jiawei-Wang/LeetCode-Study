class maze {
    int min=Integer.MAX_VALUE;
    public int min(int[][] grid,int endX,int endY){
        int coins=0;
        int m=grid.length;
        int n=grid[0].length;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==2)
                    coins++;
            }
        }
        boolean[][] visited=new boolean[m][n];
        dfs(grid,0,0,m,n,endX,endY,visited,coins,0);
        return min==Integer.MAX_VALUE?-1:min;
    }

    void dfs(int[][] grid,int i,int j,int m,int n,int endX,int endY,boolean[][] visited,int coins,int path){
        if(i<0 || j<0 || i>=m || j>=n || grid[i][j]==1 || visited[i][j]==true)
            return;
        if(i==endX && j==endY && coins==0){
            min=Integer.min(min,path);
            return;
        }
        visited[i][j]=true;
        if(grid[i][j]==2)
            coins--;
        dfs(grid,i+1,j,m,n,endX,endY,visited,coins,path+1);
        dfs(grid,i-1,j,m,n,endX,endY,visited,coins,path+1);
        dfs(grid,i,j+1,m,n,endX,endY,visited,coins,path+1);
        dfs(grid,i,j-1,m,n,endX,endY,visited,coins,path+1);
        visited[i][j]=false;
        return;
    }
    public static void main(String[] args) {
        maze b=new maze();
        int[][] grid={{0,2,1},{1,2,0},{1,0,0}};
        System.out.println(b.min(grid,2,2));
        maze b1=new maze();
        int[][] grid1={{0,2,0},{0,0,1},{1,1,1}};
        System.out.println(b1.min(grid1,1,1));
        maze b2=new maze();
        int[][] grid2={{0,1,0},{1,0,1},{1,2,2}};
        System.out.println(b2.min(grid2,1,1));
        maze b3=new maze();
        int[][] grid3={{0,2,0},{1,1,2},{1,0,0}};
        System.out.println(b3.min(grid3,2,1));
    }
}