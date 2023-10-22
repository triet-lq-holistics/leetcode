# Iterative
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    """
        Iterative:
        1. decalre a queue with default value of current root
        2. while loop,
        3. another while loop to pop root and do the below operation
        4. if root is not empty then proceed to
            5. append root.val
            6. append left and right 
    """      

    queue = [root]
    ans = []

    while queue:
        level = []
        for _ in range(len(queue)):
            root = queue[0]
            queue = queue[1:]
            
            if root:
                level.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
        if level:
            ans.append(level)
    
    return ans
        
# Recursive
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            Recursive:
            1. Each while loop we traversing thru one level. Default level as 0 
            2. if current lens(levels) == level then we create new empty array (it means that the current level hasn't been traverse yet)
            3. Append the current value to levels[level] 
            4. Recursively call left and right 
            5. Call recursive function and return
        """      

        if not root:
            return []
        
        levels = []

        def helper(root, level):
            if len(levels) == level: 
                levels.append([])
            
            levels[level].append(root.val)

            if root.left:
                helper(root.left, level+1)
            if root.right:
                helper(root.right, level+1)
        
        helper(root, 0)
        return levels
