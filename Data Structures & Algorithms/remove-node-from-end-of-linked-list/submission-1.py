# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return 

        first = head

        forward = head

        for i in range(n):
            if forward.next:

                forward = forward.next
            else:
                return head.next


        while forward and forward.next :

            forward = forward.next
            first = first.next

        first.next = first.next.next 

        return head


        