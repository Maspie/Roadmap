# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            res = 0
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)

            diameter = left+ right
            self.res = max(self.res, diameter)

            return 1 + max(left, right)
        dfs(root)
        return self.res
        
        