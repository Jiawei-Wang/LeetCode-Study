/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


//上面定义了一个TreeNode的class，这个node中有三个参数，并把val的值设为x

//BFS答案
class Solution {

    //返回的是一个2d的list
    public List<List<Integer>> levelOrderBottom(TreeNode root) {

        //Queue是一个interface，是abstract data type
        //LinkedList是一个class，是ordered data strcture
        //interface不可以直接instantiate，只能通过已存在的class
        //这个instance拥有Queue所有的operation
        Queue<TreeNode> queue = new LinkedList<TreeNode>();

        //创建一个2d的list
        List<List<Integer>> wrapList = new LinkedList<List<Integer>>();

        //如果root这个TreeNode并不存在，返回空的2dlist
        if (root == null) {return wrapList;}

        //offer()是一个不会报错版本的add()
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelNum = queue.size();

            List<Integer> subList = new LinkedList<Integer>();

            for(int i=0; i<levelNum; i++) {

                //peek()获取stack顶端元素（stack内并不删除）
                if(queue.peek().left != null) queue.offer(queue.peek().left);
                if(queue.peek().right != null) queue.offer(queue.peek().right);

                //poll()获取queue第一个元素，并删除
                subList.add(queue.poll().val);
            }

            //每次把sublist插入到wraplist的第一个位置上，其他元素向后顺移
            wrapList.add(0, subList);
        }
        return wrapList;
    }
}

/*
这个程序理解如下（2020.03）
1.queue的作用是使用BFS依次放入Tree里面的node
2.wraplist是从queue中每次取出元素后依次放在最前面得到的本题答案
3.在root不为空的情况下：即Tree中还有剩的元素
4.把当前元素放入queue，然后把每个在queue中的元素的左右子元素取出来放进去，并把这些元素放入sublist中
5.最后反顺序放进sublist
（也就是把每层的元素的子元素放进去，再把自身放进sublist中然后以一个list的形式插入wraplist）
*/


//DFS解法
public class Solution {
        public List<List<Integer>> levelOrderBottom(TreeNode root) {
            List<List<Integer>> wrapList = new LinkedList<List<Integer>>();
            levelMaker(wrapList, root, 0);
            return wrapList;
        }



        public void levelMaker(List<List<Integer>> list, TreeNode root, int level) {

            //停止levelMaker
            if(root == null) return;

            //每往tree下方走一层，往2d list的头部加入一个新linkedlist
            if(level >= list.size()) {
                list.add(0, new LinkedList<Integer>());
            }


            levelMaker(list, root.left, level+1);
            levelMaker(list, root.right, level+1);

            //get()返回位于括号内index的元素，这里是一个LinkedList，把新的元素加到linkedlist尾部
            list.get(list.size()-level-1).add(root.val);
        }
    }


/*
答案的理解：
1.wraplist是2d的list，里面的每个元素是一个linkedlist
2.一直走到leaf层，每走一层往wraplist中新建一个空的linkedlist
3.将当前的node的值，加入到对应的层的linkedlist中，然后返回上一层
*/
