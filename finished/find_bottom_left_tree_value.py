# Given the root of a binary tree, return the leftmost value in the last row of the tree.
# Input: root = [2,1,3]
# Output: 1
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

# algorithm: 
# if left exists, go down left 
# else go down right 
# if both exist, go down left then go down right 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive traversal 
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxCounter = -1
        self.leftmost = 0
        self.dfs(root, 0)
        return(self.leftmost.val)

    def dfs(self, current: TreeNode, depth: int):
        if current == None: 
            return(None)
        elif depth > self.maxCounter:
            self.maxCounter = depth 
            self.leftmost = current

        self.dfs(current.left, depth+1)
        self.dfs(current.right, depth+1)

# breadth-first traversal using a queue instead

              
