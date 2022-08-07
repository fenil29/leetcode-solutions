# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        q = [(root, False)]
        while len(q) > 0:
            curr, explored = q[-1]
            if not curr:
                q.pop()
                continue
            while curr and not explored:
                q[-1] = (curr, True)
                curr = curr.left
                q.append((curr, False))
            curr, explored = q.pop()
            if not curr:
                continue
            nums.append(curr.val)
            if len(nums) == k:
                return nums[-1]
            if curr.right:
                q.append((curr.right, False))
        return None
