# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float("-inf"), float("inf"))

    def isValidBSTHelper(self, curr, lower, upper):
        if not curr:
            return True
        if curr.val <= lower or curr.val >= upper:
            return False
        return self.isValidBSTHelper(curr.left, lower, curr.val) and self.isValidBSTHelper(curr.right, curr.val, upper)
