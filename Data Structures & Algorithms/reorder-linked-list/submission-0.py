# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        first_head = head 

        middle = head
        fast = head 

        while fast and fast.next :
            middle = middle.next
            fast = fast.next.next

        new_list = middle.next

        middle.next = None 

        prev = None 

        while new_list :

            nxt = new_list.next
            new_list.next = prev
            prev = new_list
            new_list = nxt 

        new_head = prev 

        while new_head and first_head :

            nxt1 = first_head.next

            first_head.next = new_head

            first_head = nxt1

            nxt2 = new_head.next

            new_head.next = first_head

            new_head = nxt2





        




        