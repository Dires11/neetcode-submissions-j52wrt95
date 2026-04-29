# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        stack = [root]
        while stack:
            node = stack.pop()
            left = None
            right = None
            if node.left:
                left = node.left
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                right = node.right
            node.right = left
            node.left = right
        return root
