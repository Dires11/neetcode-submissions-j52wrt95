# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True
        
        roots = [root]
        while roots:
            proot = roots.pop()
            if proot.val == subRoot.val:
                stack = [(proot, subRoot)]
                subtree = True
                while stack:
                    n1, n2 = stack.pop()
                    if not (n1 and n2) or n1.val != n2.val:
                        subtree = False
                        break
                    if n1.right or n2.right:
                        stack.append((n1.right, n2.right)) 
                    if n1.left or n2.left:
                        stack.append((n1.left, n2.left))                       
                if subtree :
                    return True
            if proot.left:
                roots.append(proot.left)
            if proot.right:
                roots.append(proot.right)
        return False
        