# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)

        cur = dummy 

        heap = []

        for i in range(len(lists)) :

            if lists[i] is None :
                continue 

            node = lists[i]

            heapq.heappush( heap , (node.val,i) )

        while heap :

            val , idx = heapq.heappop(heap)
            
            next_node = ListNode(val)

            cur.next = next_node
            cur = cur.next 

            lists[idx] = lists[idx].next

            if lists[idx] :


                heapq.heappush(heap , (lists[idx].val , idx))


        return dummy.next





        






