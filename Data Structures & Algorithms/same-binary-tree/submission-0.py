# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        
        queue1 = deque([p])
        queue2 = deque([q])
        while queue1 and queue2:
            pnode = queue1.popleft()
            qnode = queue2.popleft()
            if not (pnode and qnode):
                return False
            if pnode.val != qnode.val:
                return False
            if pnode.left or qnode.left:
                queue1.append(pnode.left)
                queue2.append(qnode.left)
            if pnode.right or qnode.right:
                queue1.append(pnode.right)
                queue2.append(qnode.right)
        return True
