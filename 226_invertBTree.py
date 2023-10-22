def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Swtich left and right in each recursion
        """

        def helper(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            helper(root.left)
            helper(root.right)
            return root
        
        return helper(root)