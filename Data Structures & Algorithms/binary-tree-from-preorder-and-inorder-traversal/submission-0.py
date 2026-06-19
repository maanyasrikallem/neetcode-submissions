# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        root = TreeNode(preorder[0])

        i = 0
        while i < len(inorder) and inorder[i] != root.val :
            i+=1 
        
        left_in = inorder[:i] 
        right_in = inorder[i+1:]

        left_pre = preorder[1:1+len(left_in)]
        right_pre = preorder[1+len(left_in):]

        root.left = self.buildTree(left_pre , left_in)
        root.right = self.buildTree(right_pre , right_in)

        return root

        





