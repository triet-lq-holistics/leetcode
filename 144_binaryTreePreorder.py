# Iterative
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
            root -> left -> right 
                 1 
                 /\
                2  3
                /\ /\
               4 5 6 7
            iteration:
            - stack: [3,2]
        """
        stack = [root]
        ans = []
        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val) 
                stack.append(root.right)
                stack.append(root.left)
                
        return ans 


# Recursive 
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
            root -> left -> right 
        """
        ls = []
        def helper(root):
            if not root:
                return 
            ls.append(root.val)
            
            left = helper(root.left)
            right = helper(root.right)
        
        
        helper(root)
        return ls 