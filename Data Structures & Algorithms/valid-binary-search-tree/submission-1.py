# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkBst(node , minim , maxim ) :

            if not node :
                return True

            if node.val <= minim or node.val >= maxim :
                return False

            return checkBst(node.left , minim , node.val) and checkBst(node.right , node.val , maxim)

        return checkBst(root , float('-inf') , float('inf')) 

        