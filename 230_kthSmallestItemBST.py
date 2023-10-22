def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            - Recursively, return immediately once match k
        """
        count = 0 
        def preorder(root):
            if not root:
                return -1
            
            nonlocal count
            
            left = preorder(root.left)
            if left != -1:
                return left
            
            count += 1
            if count == k:
                return root.val

            return preorder(root.right)
        
        return preorder(root)



def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            - Seriazlize tree -> list in pre-order traversal
            - Get kth index in the array
        """

        def preorder(root, ls: list):
            if not root:
                return ls
            
            currList = preorder(root.left, ls) + [root.val]
            return preorder(root.right, currList)
        
        treeList = preorder(root, [])
        return treeList[k-1]
