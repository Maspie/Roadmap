# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(n1, n2):

            if n1 is None and n2 is None:
                return True

            if n1 is None or n2 is None:
                return False

            if n1.val != n2.val:
                return False
            return isSame(n1.left, n2.left) and isSame(n1.right, n2.right)
        if not subRoot:
            return True         
        if not root:
            return False
        if isSame(root, subRoot):
            return True

            

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)