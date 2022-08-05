# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = deque([p])
        qQueue = deque([q])
        while len(pQueue) > 0 and len(qQueue) > 0:
            curr1, curr2 = pQueue.pop(), qQueue.pop()
            if (curr1 == None and curr2 == None):
                continue
            if curr1 == None or curr2 == None:
                return False
            if curr1.val != curr2.val:
                return False
            pQueue.append(curr1.left)
            pQueue.append(curr1.right)
            qQueue.append(curr2.left)
            qQueue.append(curr2.right)
        if len(pQueue) != 0 or len(pQueue) != 0:
            return False
        return True
