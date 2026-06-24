# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse (k , prev , node):

            if not node :
                return None 

            next_start = node

            for _ in range(k-1) :
                next_start = next_start.next 

                if not next_start :
                    return node

            cur = node

            for _ in range(k) :

                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt 

            node.next = reverse(k , None , cur)

            return prev

        return reverse(k , None , head)

  