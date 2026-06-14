# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # revise=None
        # l=[]
        # temp=head
        # while(temp):
        #     l.append(temp.val)
        #     temp=temp.next
        # l.reverse()
        # if (len(l)==0):
        #     return revise
        # revise=ListNode(val=l[0])
        # temp=revise
        # for i in range(1, len(l)):
        #     temp.next=ListNode(val=l[i])
        #     temp=temp.next
        # return revise

        prev=None
        curr=head
        while(curr):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev

        