def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        1. Clone to another linkelist
        2. Traverse thru the clone and store each val to an array
        3. Create another array and apply the formula to the store_arr to get the result in new arr
        3. Traverse thru head, starting from the second node. And assign new val for the curr node from the new arr
        """

        clone = head 
        store = []
        while clone:
            store.append(clone.val)
            clone = clone.next
        
        length      = len(store)
        re_order    = [0] * length
        re_order[0] = store[0]

        # run from 1 to middle of store arr
        # apply formula: n-i will be placed at i, and i
        i, j = 1, 1
        while j < length:
            re_order[j] = store[-i]
            if j+1 < length:
                re_order[j+1] = store[i]
            j+=2
            i+=1
        
        # # skip the first value
        head = head.next
        idx = 1
        
        # if odd, then add i*2 value from store to head.val. If even, then add store[-i]
        # For each node, update val as the corresponding re_order idx 
        while head:
            head.val = re_order[idx]
            head = head.next
            idx += 1