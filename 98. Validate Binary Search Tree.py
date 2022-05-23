# recursion，检查每个subtree是否符合left node < node < right node 
class Solution:
    def isValidBST(self, root):
        return self.check_bst(root, float("-inf"), float("inf"))

    def check_bst(self, node, left, right):
        if not node:
            return True

        if not left < node.val < right:
            return False

        return (self.check_bst(node.left, left, node.val) 
                and self.check_bst(node.right, node.val, right))
    
    '''
    初始时left = -inf，right = inf
    每次进入下一层时，根据左右subtree，将当前node的值更新为新的限制条件
    比如root的左子node的限制为：-inf < value < root.val
    假设此node = 5，则它的右子node的限制为 5 < value < root.val
    '''