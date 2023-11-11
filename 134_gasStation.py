def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        - total gas should be equal to total cost 
        - pick the starting index by examining if the gas left at that index >= 0 
        - if the total sum >= 0 and total_sum + cur diffenrece >-= 0: update total sum
        - if the total sum >= 0 and total_sum + cur difference <= 0: reset total sum  to -1
        - if total_sum == -1 and cur difference >= 0: update total_sum 
        '''

        if sum(gas) < sum(cost):
            return -1
        
        gas_left = 0
        start_idx = -1 

        for idx in range(len(gas)):
            diff = gas[idx] - cost[idx]
            
            if gas_left >= 0 and gas_left + diff >= 0:
                gas_left += diff
                start_idx = idx if start_idx == -1 else start_idx
            
            else:
                gas_left = 0
                start_idx = -1
        
        return start_idx
            
