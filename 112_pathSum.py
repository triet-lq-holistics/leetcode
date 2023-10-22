def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
             5
             /\
           9.       13
           /\.      /\
          20 None  26  8
          /\         /\
        27   22.    13 4
                        \ 
                         1
        
        - add curr val, then pass to next recursion
        - if euqal to target return true
        - if current node is None then return false
        - return recursion(left) or recursion(true)
        """

        
        def helper(root, currSum):
            if not root:
                return False
            
            currSum += root.val
            if currSum == targetSum and (not root.left and not root.right):
                return True                
            
            return helper(root.left, currSum) or helper(root.right, currSum)
        
        return helper(root, 0)