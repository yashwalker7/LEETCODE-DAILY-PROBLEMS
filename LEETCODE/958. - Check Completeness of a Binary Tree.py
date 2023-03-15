class Solution:
    def __init__(self):
        self.max_depth = -float("inf")
        self.expecting_partial = False

    def isCompleteTree(self, root: TreeNode) -> bool:

        return self.dfs(root, 0)

    def dfs(self, node, a):
        if not node:
            if self.max_depth == -float("inf"):  
                self.max_depth = a - 1
                return True
            elif self.expecting_partial:
                return a == self.max_depth
            else:
                if a == self.max_depth + 1:
                    return True
                if a == self.max_depth:
                    self.expecting_partial = True
                    return True
                return False

        return self.dfs(node.left, a + 1) and self.dfs(node.right, a + 1)
