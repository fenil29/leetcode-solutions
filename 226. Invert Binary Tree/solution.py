# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertHelper(root)
        return root

    def invertHelper(self, curr):
        if not curr:
            return
        curr.left, curr.right = curr.right, curr.left
        self.invertHelper(curr.left)
        self.invertHelper(curr.right)
