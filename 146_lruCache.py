class Node: 
    def __init__(self, val: tuple = None, prev: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    """
    How to define LRU?
    - Item that was associated the the least 
    - Maybe having a backlog of timestamp associate with the key?
    - hashmap to save the max idx of each key?

    - updateMRU: get(), put() 
    - updateLRU: when exceed capacity

    - 1 LinkedList to store recently used: LRU <-> foo1,bar1 <-> foo2,bar2 <-> foo3,bar3 <-> MRU
    - 1 hashmap: key-Node as key-val 
        {
            1: Node(foo1, bar1),
            2: Node(foo2, bar2) 
        }

    Attr:
        capacitiy: always positive
    Func:
        get() -> int:  return value if key exisit, else -1
        put() -> None: Overwrite the key-value pair. If exceed capacity then remove the least recently used key 
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.LRU, self.MRU = Node(), Node() 
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def removeLRU(self) -> None:
        """
            - Get the LRU.next
            - Get the key from LRU.next, then remove that key from cache
            - Update the LRU to the next node
                - LRU.next.next.prev = LRU
                - LRU.next = LRU.next.next 
        """
        node = self.LRU.next
        
        # Remove node in linkedlist
        self.LRU.next = node.next 
        node.next.prev = self.LRU

        # Remove key-val
        del self.cache[node.val[0]]

    
    def updateMRU(self, key: int) -> None:
        """
            - Update next and prev of node.prev and node.next
            - Update node.prev
            - Update node.next 
            - Update MRU.prev.next (next of curreent MRU)
            - Update MRU.prev
        """
        node = self.cache[key]

        # Update next and prev of node.prev and node.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # Update node
        node.prev = self.MRU.prev 
        node.next = self.MRU 
        self.MRU.prev.next = node
        self.MRU.prev = node 
        
        

    def get(self, key: int) -> int:
        """
        Return key value and and update the latest get key as MRU 
        """   
        node = self.cache.get(key)
        
        if node:
            self.updateMRU(key)
            return node.val[1] 
        
        return -1


    def put(self, key: int, value: int) -> None:
        """
        - Check if the key is already exist
            - If it is, overwrite.
            - Else, check capacity
                - if it would exceed then we remove the LRU 
                - Else, write to cache
        - Update the MRU for the key we just put 
        """
        # 1: {1: Node(1,1)} | LRU, Node(1,1), MRU           
                    # ===>  LRU <-> Node(1,1) <-> MRU 
        # 2: {2: Node(2,2)} |  LRU <-> Node(1,1) <-> MRU , Node(2,2) 
                    # ====> LRU <-> Node(1,1) <-> Node(2,2) <-> MRU 
        # 3: get(1) ====> LRU <-> Node(2,2) <-> Node(1,1) <-> MRU
        # 4: {3: Node(3,3)}: Hit capacity
                    # =====> LRU <-> Node(1,1) <-> MRU
                    # ======> LRU <-> Node(1,1) <-> Node(3,3) <-> MRU

        # Increase current index and add to timestamp metadata
        if self.cache.get(key):
            self.cache[key].val = (key, value)
        
        else:
            if len(self.cache) == self.capacity:
                self.removeLRU()
            
            self.cache[key] = Node((key,value))
        
        self.updateMRU(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)