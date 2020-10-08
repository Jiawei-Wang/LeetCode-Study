/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// 每个node拥有一个val和两个指针

// 解法1：recursion
class Solution {
    // inorder：左中右
    public List<Integer> inorderTraversal(TreeNode root) {
        // Performing various operations using List Interface and ArrayList class
        List<Integer> res = new ArrayList<>();
        helper(root, res);
        return res;
    }

    // 这个方程的意义是将tree中每个node按照次序依次放入res这个数组中
    public void helper(TreeNode root, List<Integer> res) {
        if (root != null) {
            // 理解如下：如果node有左子树，就call helper on左子树，直到最底端的那个node，将其放入list，然后返回上一级
            if (root.left != null) {
                helper(root.left, res);
            }
            res.add(root.val);
            if (root.right != null) {
                helper(root.right, res);
            }
        }
    }
}


// 解法2：Iterating method using Stack
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        // 注意 arraylist 是 list 的 interface，但是 stack 不是
        // res保存答案
        List<Integer> res = new ArrayList<>();
        // stack保存遍历node时的暂存状态
        Stack<TreeNode> stack = new Stack<>();
        // 指向root
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            // 先走到左下角
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            // 然后获得最后一个访问的node
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}
