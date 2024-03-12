def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ''' This problem is similar to detect cycle in a graph
        '''
        # Transform to hashmap of list 
        hashmap = defaultdict(list)
        for des, root in prerequisites:
            hashmap[root].append(des)

        def dfs(root, local_visited):
            nonlocal visited
            if root in local_visited:
                return False
            if root in visited:
                return True
            
            visited.add(root)
            local_visited.add(root)
            
            for des in hashmap[root]:
                if not dfs(des, local_visited): 
                    return False
            
            local_visited.remove(root)
            return True
            

        visited = set()
        # dfs check if the cur node has existed in recursion stack
        for root in list(hashmap.keys()):
            if not dfs(root, set()): 
                return False
        
        return True
