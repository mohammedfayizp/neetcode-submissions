# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final =ListNode(val=1001)
        temp=final
        c=0
        while(c<len(lists)):
            value, index=1001, -1
            for i in range(len(lists)):
                if(lists[i] is not None):
                    if(lists[i].val<value):
                        value=lists[i].val
                        index=i
            if(index!=-1):
                temp.next=ListNode(val=value)
                temp=temp.next
                lists[index]=lists[index].next
                if(lists[index] is None):
                    c+=1
        return final.next


                


        