# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([root])
        while len(q) > 0:
            currLevelVal = []
            for i in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue
                currLevelVal.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            if currLevelVal:
                ans.append(currLevelVal)
        return ans
