# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root :
            return True 

        self.not_balanced = 1

        def height(node):

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1 :
                self.not_balanced = 0

            return 1 + max(left,right)

        height(root)

        if self.not_balanced == 1:
            return True 
        else:
            return False 



        