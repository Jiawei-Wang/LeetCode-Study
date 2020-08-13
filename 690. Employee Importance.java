/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

// 读题理解：employees是一个array，里面每个元素Employee由三个子元素包含：id，权重，包含其他Employee id的array
// 给出一个id，要求返回这个Employee和它所有关联Employee的总权重
// 所以这道题其实是对树型结构/图的遍历：学习bfs和dfs的使用

// DFS
class Solution {
    Map<Integer, Employee> emap;

    // 初始化数据结构，调用helper，返回答案
    public int getImportance(List<Employee> employees, int queryid) {
        emap = new HashMap();
        for (Employee e: employees) emap.put(e.id, e);
        return dfs(queryid);
    }

    public int dfs(int eid) {
        Employee current = emap.get(eid);
        int ans = current.importance;
        // 对该employee的子employee，都同样使用helper
        for (Integer subid: current.subordinates)
            ans += dfs(subid);
        return ans;
    }
}

/*
对这个程序的理解如下：
1. 需要一个hashmap来提高查询速度，所以将元素的id和元素本身以key value pair的形式逐个放入
2. 在执行helper时：首先会对第一个子Employee调用helper，然后又对它的第一个子Employee调用helper，所以就实现了DFS
3. helper中ans这个变量：代表的是当前所在Employee和它所有子Employee的权重综合，返回给上一层
*/


// BFS
class Solution {
    public int getImportance(List<Employee> employees, int id) {
        // 同样还是先初始化一个hashmap
        Map<Integer, Employee> map = new HashMap<>();
        for (Employee employee : employees) {
            map.put(employee.id, employee);
        }

        // BFS使用队列来实现遍历
        // Queue可以使用链表或者PQ来实现
        Queue<Employee> queue = new LinkedList<>();
        // offer()是一个不报错的add()
        // 把需要查询的Employee以第一个元素的形式放入队列
        queue.offer(map.get(id));
        int total = 0;
        while (!queue.isEmpty()) {
            // poll(): return and remove first element
            Employee current = queue.poll();
            total += current.importance;
            // 将已被遍历过的元素的子元素放入队列
            for (int subordinate : current.subordinates) {
                queue.offer(map.get(subordinate));
            }
        }
        return total;
    }
}
