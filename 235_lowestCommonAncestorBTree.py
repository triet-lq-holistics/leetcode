def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            if p <= root <= q or q <= root <= p => root is the decendent
            if p,q < root => move left
            if p,q > root => move right
        """

        while root: 
            if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
                return root
            
            elif p.val < root.val and q.val < root.val:
                root = root.left
            
            elif p.val > root.val and q.val > root.val:
                root = root.right