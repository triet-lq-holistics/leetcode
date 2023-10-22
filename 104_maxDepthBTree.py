def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
            - Recursively call this function for left and right node
            - Return maximum of left and right plus 1
        """
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1