# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode(0)
        head = dummy
        nxt1 = list1
        nxt2 = list2

        while nxt1 and nxt2 :

            if nxt1.val > nxt2.val :

                head.next = nxt2
                head = nxt2
                nxt2 = nxt2.next
                

            else:

                head.next = nxt1
                head = nxt1
                nxt1 = nxt1.next

        if nxt1:

            head.next = nxt1
        
        if nxt2:
            head.next = nxt2

        return dummy.next

        