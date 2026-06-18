# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def height(node) :

            if not node :
                return 0

            return 1 + max(height(node.left) , height(node.right))

        def diam(node) :

            if not node:
                return 0 
            
            return height(node.right) + height(node.left)

        def answer(node) :

            if not node :
                return 

            self.ans = max(self.ans , diam(node))

            answer(node.left)
            answer(node.right)

            return self.ans

        return answer(root)

            

        
        
        