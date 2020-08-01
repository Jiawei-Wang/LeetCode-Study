// 读题后思路：需要注意的一点是要把每次兑换剩下的空瓶子保存起来，和下一次的空瓶子数量叠加
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        // corner case
        if (numExchange > numBottles) {
            return numBottles;
        }

        // base case
        int ans = numBottles;       // answer
        int left = numBottles;      // left over after exchange

        // exchange
        while (left >= numExchange) {
            ans += left / numExchange;
            left = left / numExchange + left % numExchange;
        }

        return ans;
    }
}
