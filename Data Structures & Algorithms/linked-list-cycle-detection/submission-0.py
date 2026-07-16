# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        cur = head
        while cur != None and cur.next != None:
            i = cur.val
            n = cur.next
            j = n.val
            if i in d:
                if d[i] == j:
                    return True
                else:
                    continue
            else:
                d[i] = j
            cur = cur.next
        if cur == None or cur.next == None:
            return False
        return True