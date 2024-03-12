def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        visited = set()
        hashmap = defaultdict(list)
        for x1,x2 in edges:
            hashmap[x1].append(x2)
            hashmap[x2].append(x1)

        def dfs(x):
            visited.add(x)
            
            for neighbor in hashmap[x]:
                if neighbor not in visited:
                    dfs(neighbor)
        if edges:
            dfs(edges[0][0])
        
        return len(visited) == n if n != 1 else True
