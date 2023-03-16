# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        a = postorder[-1]
        r = TreeNode(val=a)
        i = inorder.index(a)
        r.left = self.buildTree(inorder[:i], postorder[:i])
        r.right = self.buildTree(inorder[i + 1 :], postorder[i:-1])
        return r
