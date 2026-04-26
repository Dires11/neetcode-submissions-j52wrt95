# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        out = lists[0] 
        for i in range(1, len(lists)):
            dummy = ListNode(0)
            first = out
            second = lists[i]
            cur = dummy 
            while first and second:
                if first.val <= second.val:
                    cur.next = first
                    first = first.next
                else:
                    cur.next = second
                    second = second.next
                cur = cur.next
            if first:
                cur.next = first
            else:
                cur.next = second
            out = dummy.next
        return out
