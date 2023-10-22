# Recursive
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    """
    left -> root -> right 
            1 
            /\
        2  3
        /\ /\
        4 5 6 7
    """

    ls = []
    def helper(root):
        if not root:
            return
        
        helper(root.left)
        ls.append(root.val)
        helper(root.right)

    helper(root)
    return ls

# Iterative
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        left -> root -> right 
             1 
             /\
            2  3
            /\ /\
           4 5 6 7
             /\
            8  9
           
           [1,5]
           [4,2]
           Recursive:
           - If left and left not in ans then:
                add root to stack
                add left to stack
           - Else:
                add root to ans 
                add root.right to stack

            Iterative:
            - Push left to stack and move root to root.left until curr is null
            - Pop stack, append to ans
            - Assign root to root.right
            
            stack: [1]
            ans: [4,2,5,1]
            root: 4
        """
        

        stack = []
        ans = []

        while root or stack:
            while root: 
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        
        return ans