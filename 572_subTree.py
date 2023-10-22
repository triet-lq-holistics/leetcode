def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
            1. If root equal to subRoot, then we start to examine root and subroot
            2. If root and subroot identical, then return true
            3. Else we break, then set subRoot to its beginning point and keep traversing on root

            - Traverse in-order: root -> left -> right
        """
        def isIdentical(node1, node2) -> bool:
            stack1 = [node1.right, node1.left]
            stack2 = [node2.right, node2.left]
            while stack1 and stack2: 
                n1 = stack1.pop()
                n2 = stack2.pop()

                if n1 and n2:
                    stack1.append(n1.right)
                    stack1.append(n1.left)
                    stack2.append(n2.right)
                    stack2.append(n2.left)
                
                elif not n1 and not n2:
                    continue

                if (not n1 or not n2) or n1.val != n2.val:
                    return False
                
            return True


        stack = [root]
        while stack:
            node = stack.pop()
   
            if node and node.val == subRoot.val and isIdentical(node, subRoot):
                    return True

            if node:
                stack.append(node.right)
                stack.append(node.left)
        
        return False
            