class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        id: 123
        val
        random 



        1. loop thru head 
        2. copy head val to dummy val
        3. random -> Node => create a random Node, then assign to dummy.node
        4. create an empty dummy and assign to dummy.next
        5. set curr dummy to None
        
        1000, null
        1002, 1000
        1004, 1008
        1006, 1002
        1008, 1000

        1000: random = None, idx = 0, clone = 2000
        1002: random = 1000, idx = 1, clone = 2002
        1004: random = 1008, idx = 2, clone = 2004
        1006: random = 1002, idx = 3, clone = 2006
        1008: random = 1000, idx = 4, clone = 2008

        [None, 0, 4, 1, 0]
        
        [None, Node(7, next, random), Node(...), Node(...), Node(...)]

        Naive:
        - First loop to get next val
            1. loop thru head
            2. val: assign head val

        - Second loop to assign random
            3. random: 
                a. if None then assign None
                b. else 
        """
        if not head:
            return None

        dummy = Node(0)
        clone = Node(-1) 
        dummy.next = clone 
        randoms = {}

        idx = 0
        nodes = []
        while head:
            clone.val = head.val 
            clone.next = Node(-1)
            nodes.append(clone)

            randoms[id(head)] = dict(
                idx     = idx,
                random  = id(head.random) if head.random else None,
                clone   = clone
            )
            
            clone = clone.next
            head = head.next
            idx += 1

        links = [randoms[val.get('random')].get('idx') if val.get('random') else None for val in randoms.values()]
        clone.next = None
        clone = dummy.next
        

        for i in range(len(nodes)):
            link = links[i]
            clone.random = nodes[link] if link is not None else None

            if i < len(nodes) - 1:
                clone = clone.next
            else:
                clone.next = None

        return dummy.next


def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    links = {None: None}
    # Loop thru head and set key-value of old-new node to hashmap

    clone = head 
    while clone:
        copy = Node(clone.val)
        links[clone] = copy

        clone = clone.next
    
    # Loop thru head again and set next and random value of copy linklist
    clone = head
    while clone:
        copy = links[clone]
        copy.next = links[clone.next]
        copy.random = links[clone.random]

        clone = clone.next
    
    return links[head]