def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
            - level-order traversal
            - get the very last item of each level
            Algo: 
            - Pop every item of dequeu
            - append left and right child to the queue again
            - add each item value to a list
            - append list to levels 
        """
        levels = []
        q = deque([root])

        while q:
            ls = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    ls.append(node.val)
            
            levels.append(ls)
        

        return [level[-1] for level in levels[:-1]]