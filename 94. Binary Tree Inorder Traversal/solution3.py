class Solution:
    def inorderTraversal(self, root: Optional[TreeNode],) -> List[int]:
        nums = []
        q = [(root, False)]
        # print(q)
        while len(q) > 0:
            curr, seen = q[-1]
            if not curr:
                q.pop()
                continue
            while curr and not seen:
                q[-1] = (curr, True)
                curr = curr.left
                q.append((curr, False))
            curr, seen = q.pop()
            if not curr:
                continue
            nums.append(curr.val)
            if curr.right:
                q.append((curr.right, False))
        return nums
