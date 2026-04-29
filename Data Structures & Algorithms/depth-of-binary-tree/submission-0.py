# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = 1
        stack = [(root, depth)]
        while stack:
            node, cur_depth = stack.pop()
            depth = max(depth, cur_depth)
            if node.left:
                stack.append((node.left, cur_depth+1))
            if node.right:
                stack.append((node.right, cur_depth+1))
        return depth