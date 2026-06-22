# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head 

        before_left = dummy
        right = dummy


        for _ in range(l-1) :

            before_left = before_left.next 
        
        left = before_left.next 
        last = left 

        for _ in range(r) :

            right = right.next

        after_right = right.next 

        prev = None 

        while prev != right :

            nxt = left.next

            left.next = prev 

            prev = left 

            left = nxt 

        last.next = after_right

        before_left.next = prev 

        return dummy.next
            
        


        