def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            2 check:
                left < root.val < right
                right.val should not larger than the most recent largest value
                left value should not smaller than the most recent smallest value 

            => left bound < left.val < root.val < right.val < right.bound
        """
        
        def helper(root, left_bound, right_bound):
            if not root:
                return True
            
            if root.left and not left_bound < root.left.val < root.val:
                return False
            
            if root.right and not right_bound > root.right.val > root.val:
                return False

            
            left_bool = helper(root.left, left_bound, root.val) 
            right_bool = helper(root.right, root.val, right_bound)
            
            return left_bool and right_bool
        
        return helper(root, float('-inf'), float('inf'))