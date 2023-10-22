def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        """
        - Post-order traversal
        - Handle null value 
        - Check if current subtree has all values the same
            - Store in an array and return? 
            - if true, then count += 1
        
        """
        
        self.ans = 0 
        def helper(root) -> list:
            if not root:
                return []
            subTree = helper(root.left) + helper(root.right) + [root.val]
            
            if subTree.count(subTree[0]) == len(subTree):
                self.ans += 1
            
            return subTree
        
        helper(root)
        return self.ans
