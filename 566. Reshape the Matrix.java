class Solution {
  public int[][] matrixReshape(int[][] nums, int r, int c) {
    int n = nums.length, m = nums[0].length;
    if (r * c != n * m) {
      return nums;
    }
    int[][] answer = new int[r][c];
    for (int i = 0; i < r * c; i ++) {
      // i-th element has fixed position in both lists
      answer[i/c][i%c] = nums[i/m][i%m];
    }
    return answer;
  }
}
