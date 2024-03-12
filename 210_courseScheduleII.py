def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''Kahn algo'''
        # List of degree 
        degrees = [0] * numCourses
        lookup = defaultdict(list)
        for des, root in prerequisites:
            degrees[des] += 1
            lookup[root].append(des)

        print(degrees)
        print(lookup)
        # Find all the 0 degree's node, put it to queue.
        # Pop the queue, then decrease all the destination of popped node
        # repeat the step until the queue is empty 
        queue = deque()
        visited = set()
        res = []
        while True:
            for node, degree in enumerate(degrees):
                if degree == 0 and node not in visited:
                    queue.append(node)
                    visited.add(node)
            
            if len(queue) == 0:
                break
                
            cur_node = queue.popleft()
            res.append(cur_node)
            degrees[cur_node] = -1
            
            for des in lookup[cur_node]:
                degrees[des] -= 1
        
        # Check if all the number in the list of degree is equal to zero
        # Return list, else return none
        for degree in degrees:
            if degree > 0: return None
        return res 
