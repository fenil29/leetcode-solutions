# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode],) -> List[int]:
        return self.inorderTraversalHelper(root, [])

    def inorderTraversalHelper(self, curr, ans):
        if not curr:
            return
        self.inorderTraversalHelper(curr.left, ans)
        ans.append(curr.val)
        self.inorderTraversalHelper(curr.right, ans)
        return ans
