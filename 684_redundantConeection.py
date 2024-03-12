def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''Union find. If the new pair is not connected already, replace the result'''
        roots = [i for i in range(len(edges)+1)]
        ranks = [1] * (len(edges)+1)
        # Find  - Path compression
        ## Base case: If root equal to itsel, then return itself
        ## Else we assign the current root to its recursive call
        ## So the next time we call, this node will point to its original root right away
        def find(x):
            if roots[x] == x:
                return x
            roots[x] = find(roots[x])
            return roots[x]

        # Union 
        ## Default rank as 1 for every node
        ## If rank is equal -> Assign root one node, and increase rank of the other by 1 
        ## Else then assign root to the smaller one 
        def union(x1, x2):
            root1 = find(x1)
            root2 = find(x2)

            if root1 == root2:
                return 
            
            if ranks[root1] < ranks[root2]:
                roots[root1] = root2
            elif ranks[root1] > ranks[root2]:
                roots[root2] = root1
            else:
                roots[root1] = root2
                ranks[root2] += 1

        def connected(x1, x2):
            return find(x1) == find(x2)
        
        ## Check if 2 node of the edge have the same root, then replace the current res, and union 
        res = None
        for x1, x2 in edges:
            if connected(x1,x2):
                print(x1, x2, find(x1), find(x2))
                res = [x1,x2]
            union(x1,x2)

        return res

