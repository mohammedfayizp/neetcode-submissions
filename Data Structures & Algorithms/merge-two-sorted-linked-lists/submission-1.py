# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not list1):
            return list2
        if(not list2):
            return list1
        c1, c2=list1,list2
        if(list1.val<=list2.val):
            head=list1
            c1=c1.next
        else:
            head=list2
            c2=c2.next
        start=head
        
        while(c1 and c2):
            if(c1.val<=c2.val):
                head.next=c1
                c1=c1.next
            else:
                head.next=c2
                c2=c2.next
            head=head.next
        while(c1):
            head.next=c1
            c1=c1.next
            head=head.next
        while(c2):
            head.next=c2
            c2=c2.next
            head=head.next
        return start
        


        