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
        return(self.returned)
    
    def isEven(self, row:[[int]]):
        for i in row: 
            if i % 2 == 1: 
                self.isEvenOdd = False
                print("Is Even % ", row, self.isEvenOdd)
                return
        proper = list(reversed(sorted(list(set(row)))))
        if proper != row: 
            self.isEvenOdd = False
            print("Even sorted", proper)
            print("Is Even ", row, self.isEvenOdd)
            return

    def isOdd(self, row:[[int]]): 
        for i in row: 
            if i % 2 == 0: 
                self.isEvenOdd = False
                print("Is Odd % ", row, self.isEvenOdd)
                return
        proper = sorted(list(set(row)))
        if proper != row: 
            self.isEvenOdd = False
            print("Odd sorted", proper)
            print("Is Odd ", row, self.isEvenOdd)
            return
    
    def isEvenOddTree(self, root: [TreeNode]) -> bool:
        self.isEvenOdd = True
        full_tree = self.levelOrderBottom(root) 
        if full_tree == []: 
            return False
        else: 
            for i in range(len(full_tree)):
                print(i)
                if i % 2 == 0: 
                    self.isOdd(full_tree[i])
                else: 
                    self.isEven(full_tree[i])
                
        return(self.isEvenOdd)
        
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
        
# test1 = TreeNode(val=3, left=TreeNode(9, None, None), right=TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
# test2 = TreeNode(1, None, None)
# test3 = TreeNode(None, None, None)
# test4 = TreeNode(1, TreeNode(2, None, TreeNode(4, None, None)), TreeNode(3, TreeNode(5, None, None), None))
# print(Solution().levelOrderBottom(test1))
# print(Solution().levelOrderBottom(test2))
# print(Solution().levelOrderBottom(test3))
# print(Solution().levelOrderBottom(test4))