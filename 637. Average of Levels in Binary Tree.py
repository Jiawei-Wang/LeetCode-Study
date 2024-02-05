# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    if not root:
      return None
    
    currentLevel = [root]
    nextLevel = []
    answer = []

    while currentLevel:
      index = 0
      total = 0
      while index < len(currentLevel):
        node = currentLevel[index]
        total += node.val 
        if node.left: nextLevel.append(node.left) 
        if node.right: nextLevel.append(node.right) 
        index += 1
      answer.append(total/index)
      currentLevel = nextLevel
      nextLevel = []
    
    return answer
    
# optimize 
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        currentLevel = [root]
        answer = []

        while currentLevel:
            total = 0
            num_nodes = len(currentLevel)  # Track the number of nodes in the current level
            nextLevel = []
            for node in currentLevel:
                total += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            answer.append(total / num_nodes)  # Calculate average using the number of nodes
            currentLevel = nextLevel

        return answer

    
      

        