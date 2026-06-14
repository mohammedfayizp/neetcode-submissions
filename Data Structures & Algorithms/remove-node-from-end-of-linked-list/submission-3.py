# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while(temp):
            count+=1
            temp=temp.next
        n=count-n+1
        temp=head
        if(n==1):
            head=head.next
            return head
        for i in range(1, n+1):
            if(i==n-1):
                check=None
                if(temp.next.next):
                    check=temp.next.next
                temp.next=check
                break
            temp=temp.next
        return head

        
        
        