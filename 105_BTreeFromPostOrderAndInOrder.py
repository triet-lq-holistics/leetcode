def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            preorder: root always starts first 
            inorder: 2 sides are separated by the root 
            [3,9, 20]
            [9,3, 15]

            3 as first item in preorder => 2 sides of tree = [9] | 3  | [15,20,7] in inorder 
                => root = 3 | because left side is not empty => next value in preorder going to be left 
                [15,9,20]
            9 as second item -> 2 sides of tree = [] | 9 | [] =>  
            20 => 2 sides of tree -> 15 | 20 | 7
            15 => 2 sides of tree => [] | 15 | []
            7 => 2 sides of tree => [] | 7 | []

            - keep track of left and right side
            - able to identify which side it is of the next value in preorder list
            - Send the corresponding subtree to the next operation

            [3,9,20,15,7]
             ^ ^ ^  ^  
            
            0, [9,3,15,20,7] | [3] -> [9] | 3 | [15,20,7]. Pass 1. Get 1. Pass 2. Return 4
                1, [9] | [9] -> None | 9 | None . Return 
                2. [15,20,7] | [20] -> [15] | 20 | [7]. Pass 3. Get 3. Pass 4. Return 4
                    3. [15] | [15] -> None | 15 | None. Return 3
                    4. [7] .............................  Return 4.

                Return subtree

            
            20: 3

            [9,3,15,20,7], rootIdx = 1, leftBound = 2, rightBound = 4
            [15, 20, 7], 
            
        """
        idx = 0 
        d = {inorder[i]: i for i in range(len(inorder))}

        def helper(leftBound, rightBound):
            """
            Instead of loop thru preorder, we use recursion with incremental index 
            """
            nonlocal idx

            
            # Assign current root.val as current recursive value 
            root = TreeNode(preorder[idx])
            
            # Index of this roort.val in inorder
            rootIdx = d[root.val]
            
            # Get left side and right side of root.val
            leftSide = inorder[leftBound:rootIdx]
            rightSide = inorder[rootIdx+1:rightBound]
            idx += 1

            # If leftside is not empty, then get the left subtreee
            if leftSide:
                root.left = helper(leftBound, rootIdx)
            
            # If rightside is not empty then get the right subtree
            if rightSide:
                root.right = helper(rootIdx+1, rightBound)

            return root

        return helper(0, len(inorder))