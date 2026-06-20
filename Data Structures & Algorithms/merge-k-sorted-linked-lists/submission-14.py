# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # final =ListNode(val=1001)
        # temp=final
        # c=0
        # while(c<len(lists)):
        #     value, index=1001, -1
        #     for i in range(len(lists)):
        #         if(lists[i] is not None):
        #             if(lists[i].val<value):
        #                 value=lists[i].val
        #                 index=i
        #     if(index!=-1):
        #         temp.next=lists[index]
        #         temp=temp.next
        #         lists[index]=lists[index].next
        #         if(lists[index] is None):
        #             c+=1
        # return final.next

        final =ListNode(val=0)
        temp=final
        lookup=[]
        for i in range(len(lists)):
            if(lists[i] is not None):
                heapq.heappush(lookup,(lists[i].val,i))
        while(len(lookup)):
            value, index= heapq.heappop(lookup)
            temp.next=lists[index]
            temp=temp.next
            if(lists[index].next is not None):
                lists[index]=lists[index].next
                heapq.heappush(lookup,(lists[index].val, index))
        return final.next
        



                


        