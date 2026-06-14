# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count=0
        temp=head
        while(temp):
            count+=1
            temp=temp.next
        last=None
        temp=head
        left=head
        right=None
        c=0
        while(temp):
            c+=1
            temp=temp.next
            if(c==count//2):
                right=temp.next
                temp.next=None
                break
        prev=None
        curr=right
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        start=left
        l = left
        p = prev

        while p:
            next_l = l.next
            next_p = p.next

            l.next = p
            p.next = next_l

            l = next_l
            p = next_p
        head=start


        
            
            

            
        

        

        