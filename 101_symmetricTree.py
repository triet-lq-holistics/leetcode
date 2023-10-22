def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        inorder traversal left and reverse inorder traversal right, then compare the 2 
        """

        left = [] 
        stack = [root.left]
        while stack:
            node = stack.pop()
            val = node.val if node else None
            left.append(val)
            
            if node:
                stack.append(node.right)    
                stack.append(node.left)
        
        right = []
        stack = [root.right]
        while stack:
            node = stack.pop()
            val = node.val if node else None
            right.append(val)
            
            if node:
                stack.append(node.left)    
                stack.append(node.right)

        return left == right

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive
        - Compare left val and right val
        """

        def helper(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            
            return left.val == right.val and \
                helper(left.left, right.right) and\
                helper(left.right, right.left)
        
        return helper(root, root)