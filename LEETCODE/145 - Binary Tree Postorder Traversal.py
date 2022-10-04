class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         def dfs(root,res):
            if root is None: return []
            dfs(root.left, res)
            dfs(root.right, res)
            res.append(root.val)
            return res
         return dfs(root, [])