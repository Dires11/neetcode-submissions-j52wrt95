"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        headpointer = head
        dummyNode = Node(0)
        addresses = {}
        copyNode = dummyNode
        while head:
            copyNode.next = Node(head.val)
            addresses[head] = copyNode.next
            copyNode = copyNode.next
            head = head.next
            
        copyNode = dummyNode.next
        head = headpointer
        while head:
            if head.random:
                copyNode.random = addresses[head.random]    
            else:
                copyNode.random = None
            head = head.next
            copyNode = copyNode.next
        return dummyNode.next


