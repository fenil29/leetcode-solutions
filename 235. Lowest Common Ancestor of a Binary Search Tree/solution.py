# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
        currP = root
        currQ = root
        while(currP != p or currQ != q):
            if (currP == currQ):
                ans = currP
            if currP.val > p.val:
                currP = currP.left
            elif currP.val < p.val:
                currP = currP.right
            if currQ.val > q.val:
                currQ = currQ.left
            elif currQ.val < q.val:
                currQ = currQ.right
        return ans
