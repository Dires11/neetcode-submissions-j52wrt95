# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([[root]])
        out = []
        while queue:
            row = queue.popleft()
            newrow = []
            out.append(row[-1].val)
            for i in range(len(row)):
                if row[i].left:
                    newrow.append(row[i].left)
                if row[i].right:
                    newrow.append(row[i].right)
            if newrow: queue.append(newrow)
        return out
        