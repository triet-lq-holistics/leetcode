def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calc diameter:
            - left's depth + right's depth 
        
        - Return level from bottom up
        - Add left and right level, then compare to the maximum height
        """
        maxDiameter = 0

        def helper(root):
            nonlocal maxDiameter 
            if not root:
                return 0
            
            left, right =  helper(root.left), helper(root.right)
            currDiameter = left + right
            maxDiameter = max(maxDiameter, currDiameter)

            return max(left,right) + 1 

        helper(root)

        return maxDiameter
