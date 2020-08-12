// 读题想法：最短路径题，同时加上了edge上限的限制
// 学习他人的解法

// 解法1：PQ，此答案以python版作为模板修改
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        // 首先将array转为hashmap
        // 需要声明prices是一个2d hashmap
        Map<Integer, Map<Integer, Integer>> prices = new HashMap<>();
        // flights也是一个2d array
        for (int[] f : flights) {
            // 对于prices来说，如果不含f[0]（也就是说这个点目前还没放进去过），那就需要为其新建一个hashmap
            if (!prices.containsKey(f[0])) prices.put(f[0], new HashMap<>());
            // 在f[0]的value（也就是f[0]的那个hashmap)中放入key-value pair
            prices.get(f[0]).put(f[1], f[2]);
            // get(): 获得value；put(): 更新value
        }

        TODO: 下面部分还没有理解
        // 前半句的意思是创建一个新的PQ，每个元素是一个int array
        // 后半句是一个lambda expression: operator -> body
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> (Integer.compare(a[0], b[0])));
        pq.add(new int[] {0, src, k + 1});
        while (!pq.isEmpty()) {
            int[] top = pq.remove();
            int price = top[0];
            int city = top[1];
            int stops = top[2];
            if (city == dst) return price;
            if (stops > 0) {
                Map<Integer, Integer> adj = prices.getOrDefault(city, new HashMap<>());
                for (int a : adj.keySet()) {
                    pq.add(new int[] {price + adj.get(a), a, stops - 1});
                }
            }
        }
        return -1;
    }
}
