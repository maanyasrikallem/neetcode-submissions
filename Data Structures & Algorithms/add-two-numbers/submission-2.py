# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        head = ListNode(0)
        dummy = head 

        carry = 0

        while l1 and l2 :

            nxt1 = l1.next
            nxt2 = l2.next

            val = l1.val + l2.val + carry 

            num = val%10 
            carry = val//10

            head.next = ListNode(num)
            head = head.next

            l1 = nxt1
            l2 = nxt2

        while l1 :

            nxt1 = l1.next

            val = l1.val + carry

            num = val%10
            carry = val//10

            head.next = ListNode(num)
            head = head.next

            l1 = nxt1

        while l2 :

            nxt2 = l2.next

            val = l2.val + carry

            num = val%10
            carry = val//10

            head.next = ListNode(num)
            head = head.next

            l2 = nxt2


        if carry !=0 :
            head.next = ListNode(carry)
        

        return dummy.next


        