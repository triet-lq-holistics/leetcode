def goodNodes(self, root: TreeNode) -> int:
        """
        - Count current node if current node is equal > larger than ancestor node's val 
        """

        count = 0
        def helper(root, maxVal):
            if not root:
                return 
            
            elif root.val >= maxVal:
                nonlocal count
                count += 1
                maxVal = root.val
            
            helper(root.left, maxVal)
            helper(root.right, maxVal)
        
        
        helper(root, root.val)
        return count