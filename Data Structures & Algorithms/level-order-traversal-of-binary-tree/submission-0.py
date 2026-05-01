# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        count = 1
        out = []
        while queue:
            newcount = 0
            row = []
            for i in range(count):
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    newcount += 1
                    queue.append(node.left)
                if node.right:
                    newcount += 1
                    queue.append(node.right)
            count = newcount
            out.append(row)
        return out