# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(p,q) :

            if not p and not q :
                return True

            if (p and not q) or (q and not p) :
                return False

            if p.val != q.val :
                return False

            a = same(p.left , q.left)
            b = same(p.right , q.right)

            return a and b 

        def find(node):

            a = False 

            if not node :
                return False

            if node.val == subRoot.val :

                a = same(node,subRoot)

            if a :
                return True 

            return find(node.left) or find(node.right)
        
        return find(root)

            

        
        