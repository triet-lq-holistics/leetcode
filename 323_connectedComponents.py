def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''Union Find. Then return unique number in roots'''
        roots = [i for i in range(n)]
        ranks = [1] * n

        def find(x):
            if roots[x] == x:
                return x
            roots[x] = find(roots[x])
            return roots[x]

        def union(x1, x2):
            root1 = find(x1)
            root2 = find(x2)

            if root1 == root2:
                return
            
            if ranks[root1] > ranks[root2]:
                roots[root2] = root1 
            
            elif ranks[root2] > ranks[root1]:
                roots[root1] = root2 
            else:
                roots[root1] = roots[root2]
                ranks[root2] += 1



        unique = set()
        for x1,x2 in edges:
            union(x1, x2)
        
        for root in roots:
            unique.add(find(root))
        
        return len(unique)
