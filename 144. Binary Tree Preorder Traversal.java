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

// preorder: 中左右

// 解法1：recursion
// Time: n
// Space: n
// 具体实现：stack + 被多次压入stack的helper
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        // 1.创建新list，2.call helper，3.return list
        List<Integer> ans = new ArrayList<>();
        preorder(root,ans);
        return ans;
    }

    private void preorder(TreeNode root, List<Integer> ans) {
        // corner case
        if (root == null) {
            return;
        }
        // 先中，再左，最后右，左右均为子树，所以再call一次helper即可
        ans.add(root.val);
        preorder(root.left, ans);
        preorder(root.right,ans);
    }
}


// iteration
// Time: n
// Space: n 使用stack来储存node
// 具体实现：使用while循环走到最左下角，然后依次从stack中取出右子树再进入其中
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();

        // 注意这里停止的条件是Tree和stack都为空
        while (root != null || !stack.empty()) {
            // 先沿着左侧一直向下直到最左下角，同时把每一层的右子树暂存在stack中
            if (root != null) {
                ans.add(root.val);
                if (root.right != null) {
                    stack.push(root.right);
                }
                root = root.left;
            // 等到到了最左下角后，将之前存储的右子树拿出来
            } else {
                root = stack.pop();
            }
        }
        return ans;
    }
}
