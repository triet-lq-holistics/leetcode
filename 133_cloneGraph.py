from typing import Optional
class Solution:
    visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
            - change as you go 
            - clone the current node
            - if the current neighbor val exist in visited ,then add that key-value to neighbors
            - else, append the recursive clone node of this neighbor to neighbors
            - return the clone node 
        '''
        if not node:
            return node
        
        clone_node = Node(node.val)
        self.visited[node] = clone_node 
        
        
        for neighbor in node.neighbors:
            if neighbor in self.visited:
                clone_node.neighbors.append(self.visited[neighbor])
            else:
                clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node
