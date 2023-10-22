def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
            keep track of 
            - height of left and right
            - whether it is balanced in the downstream
        """
        def helper(root) -> tuple[int, bool]:
            if not root: 
                return (0, True)
            
            left = helper(root.left)
            right = helper(root.right)

            isBalanced = abs(left[0] - right[0]) <= 1
            height = max(left[0], right[0])

            return (height+1, isBalanced and left[1] and right[1])
        

        res = helper(root)
        return res[1]