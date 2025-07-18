# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, min, max):

                if not node:
                    return True

                if not (min < node.val < max):
                    return False

                left = valid(node.left, min, node.val)
                right = valid(node.right, node.val, max)

                return left and right

        return valid(root, float("-inf"), float("inf"))
        