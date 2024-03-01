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



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive solution 
class Solution:
    def levelOrderBottom(self, root:[TreeNode]) -> [[int]]:
        self.maxdepth = -1
        self.returned = [] 
        if root: 
            self.returned.append([])
            self.recursive(root, 0)
        return(list(reversed(self.returned)))
        
    def recursive(self, current:[TreeNode], depth): 
        if current == None: 
            return
        else: 
            if depth > self.maxdepth: 
                self.maxdepth = depth
            # print(current.val)
            if depth >= len(self.returned): 
                self.returned.append([])
            self.returned[depth].append(current.val)
            # print(self.returned)
            # print(depth)
            if current.left != None or current.right != None: 
                # self.depth += 1
                if current.left: 
                    # print("Left: " + str(current.left.val))
                    self.recursive(current.left, depth+1)
                if current.right: 
                    # print("Right: " + str(current.right.val))
                    self.recursive(current.right, depth+1)
            return

# Trying a breadth-first based solution 
# class Solution:
#     def levelOrderBottom(self, root:[TreeNode]) -> [[int]]:
#         returned = []
#         queue = [] 
#         queue.append(root) 
#         if root != None:
#             returned.append([root.val])

#         while queue: 
#             current = queue.pop(0)
#             to_be_added = []
#             if current != None:
#                 if current.left != None: 
#                     to_be_added.append(current.left.val)
#                     queue.append(current.left)
#                 if current.right != None: 
#                     to_be_added.append(current.right.val)
#                     queue.append(current.right)
#                 if to_be_added != []:
#                     returned.append(to_be_added)

#         return(list(reversed(returned)))


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
        
test1 = TreeNode(val=3, left=TreeNode(9, None, None), right=TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
test2 = TreeNode(1, None, None)
test3 = TreeNode(None, None, None)
test4 = TreeNode(1, TreeNode(2, None, TreeNode(4, None, None)), TreeNode(3, TreeNode(5, None, None), None))
print(Solution().levelOrderBottom(test1))
print(Solution().levelOrderBottom(test2))
print(Solution().levelOrderBottom(test3))
print(Solution().levelOrderBottom(test4))