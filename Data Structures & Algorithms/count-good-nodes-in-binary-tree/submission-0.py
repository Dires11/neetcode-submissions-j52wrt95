# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar=float('-inf')):
            if not node: return 0            
            return int(node.val >= maxSoFar) + dfs(node.left, max(maxSoFar, node.val)) + dfs(node.right, max(maxSoFar, node.val))
        return dfs(root)