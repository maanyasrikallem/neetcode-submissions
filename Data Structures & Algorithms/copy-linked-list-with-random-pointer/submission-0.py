class Solution:
    def copyRandomList(self, head):

        if not head:
            return None

        old_to_new = {None: None}

        curr = head

        # Create all nodes
        while curr:

            copy = Node(curr.val)

            old_to_new[curr] = copy

            curr = curr.next

        curr = head

        # Connect next and random
        while curr:

            copy = old_to_new[curr]

            copy.next = old_to_new[curr.next]

            copy.random = old_to_new[curr.random]

            curr = curr.next

        return old_to_new[head]