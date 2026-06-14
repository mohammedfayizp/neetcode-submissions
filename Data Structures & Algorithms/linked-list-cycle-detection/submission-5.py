# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1, p2=head, head
        if(not p1 and not p2):
            return False
        if(p2.next):
            p2=p2.next
        else:
            return False

        while(p1!=p2):
            if(p1.next):
                p1=p1.next
            else:
                return False
            if(p2.next):
                p2=p2.next
            else:
                return False
            if(p2.next):
                p2=p2.next
            else:
                return False
        return True
            
        