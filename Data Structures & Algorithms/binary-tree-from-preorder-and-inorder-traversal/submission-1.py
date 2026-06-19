# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indexing = {val: i for i, val in enumerate(inorder)}

        n = len(preorder)

        def helper(lp, rp, li, ri):

            if lp >= rp:
                return None

            root = TreeNode(preorder[lp])

            i = indexing[root.val]

            left_size = i - li

            root.left = helper(
                lp + 1,
                lp + 1 + left_size,
                li,
                i
            )

            root.right = helper(
                lp + 1 + left_size,
                rp,
                i + 1,
                ri
            )

            return root

        return helper(0, n, 0, n)