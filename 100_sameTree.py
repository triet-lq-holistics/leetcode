def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        "Recursive"
        if not p and not q:
           return True
        elif not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)


def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        "Iterative: Check node in BFS style"
        def is_same(p, q):
            if not p and not q:
                return True
            
            elif not p or not q:
                return False
        
            return p.val == q.val 



        queue = deque([(p,q)])

        while queue:
            p,q = queue.popleft()
            if not is_same(p,q):
                return False
            
            if p and q:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        
        return True
        