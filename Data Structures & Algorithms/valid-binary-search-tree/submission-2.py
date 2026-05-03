# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, max_bound=float('inf'), min_bound=float('-inf')):
            if not root: return True
            if root.val >= max_bound:
                return False
            if root.val <= min_bound: 
                return False
            left = dfs(root.left, max_bound=root.val, min_bound=min_bound)
            right = dfs(root.right, max_bound=max_bound, min_bound=root.val)
            return left and right 
        return dfs(root)          