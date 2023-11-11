def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        0. Init a heap from unique number of hand to extract the minimum val for each group
        1. for each group, from the current min, looking for its consecutive number
        2. if exist, then minus it by 1
            2a. if its count == 0, then we pop the min key from the heap
        3. else, return False 
        '''

        if (len(hand) % groupSize) != 0 :
            return False

        counter = Counter(hand)
        keys = list(counter.keys())
        heapq.heapify(keys)

        for _ in range((len(hand) // groupSize)):
            cur_num = keys[0]
            
            for _ in range(groupSize):
                if counter.get(cur_num):
                    counter[cur_num] -= 1
                    
                    if counter[cur_num] == 0: heapq.heappop(keys)
                    cur_num += 1

                else: 
                    return False
            
        return True
