# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (i.e., from left to right, level by level from leaf to root).

# Example 1: 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Example 4: 
# root =
# [1,2,3,4,null,null,5]

# 1 
# | | 
# 2 3 
# | | 
# 4 5 

# Use Testcase
# Output
# [[5],[4],[2,3],[1]]
# Expected
# [[4,5],[2,3],[1]]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Trying a breadth-first based solution 
class Solution:
    def levelOrderBottom(self, root:[TreeNode]) -> [[int]]:
        returned = []
        queue = [] 
        queue.append(root) 
        if root != None:
            returned.append([root.val])

        while queue: 
            current = queue.pop(0)
            to_be_added = []
            if current != None:
                if current.left != None: 
                    to_be_added.append(current.left.val)
                    queue.append(current.left)
                if current.right != None: 
                    to_be_added.append(current.right.val)
                    queue.append(current.right)
                if to_be_added != []:
                    returned.append(to_be_added)

        return(list(reversed(returned)))

test1 = TreeNode(val=3, left=TreeNode(9, None, None), right=TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
test2 = TreeNode(1, None, None)
test3 = TreeNode(None, None, None)
print(Solution().levelOrderBottom(test1))
print(Solution().levelOrderBottom(test2))
print(Solution().levelOrderBottom(test3))