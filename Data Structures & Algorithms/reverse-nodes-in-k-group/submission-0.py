# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        while True:
            groupEnd = prevGroup
            for i in range(k):
                groupEnd = groupEnd.next
                if not groupEnd:
                    return dummy.next
            
            groupStart = prevGroup.next
            prev = groupEnd.next
            cur = groupStart
            for i in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            prevGroup.next = prev
            prevGroup = groupStart
        
            
