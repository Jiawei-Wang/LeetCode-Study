/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def findTarget(root: TreeNode, k: Int): Boolean = {
    // Use a hash set to store visited values
    var numSet: Set[Int] = Set.empty 

    // Helper function to perform DFS
    def dfs(node: TreeNode): Boolean = {
      if (node == null) return false
      // Check if the complement of current node value exists in the set
      if (numSet.contains(k - node.value)) return true
      // Add current node value to the set
      numSet += node.value
      // Recursively check left and right subtrees
      dfs(node.left) || dfs(node.right)
    }

    // Start DFS from the root
    dfs(root)
  }
}
