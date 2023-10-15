def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        To get number of days to get warmer, i need to know what the latest succeeding day is warmer for the curr day 
        Naive
        1. Create an array to store the next index that is warmer subject to the current day 
            a. For loop thru temps.
            b. Nested for loop and stop whenever get the warmer day 
        2. Create another array that subtract next index to curr index to get day diff 
        Complexity:
            O((n-1) * (n-2)) = O(n*2)

        Monotonic Decreasing Stack
        - Idea: We want to store the previous day temp and and moving forward at the same time. So we'll use stack. Since tracing value from idx is constant time so we will keep track of the idx in the stack only
        - Algo:
            1. If the next temp is equal or smaller the top stack value, then we push it to stack. 
            2. Else we pop the top value until hitting an equal or larger top value, or until stack is empty. 
            3. The pop item will be inserted to the ans arr at the index the same as the pop item. The inserted value is the diff between the curr item/top stack item and this pop item
            4. Push currTemp to the stack once while loop complete
        """

        waitDays = [0] * len(temperatures)
        stack = [] 

        for currDay, currTemp in enumerate(temperatures):
            if (not stack) or (currTemp <= temperatures[stack[-1]]):
                stack.append(currDay)
            else:
                while len(stack) > 0 and currTemp > temperatures[stack[-1]]:
                    day = stack.pop()
                    waitDays[day] = currDay - day
                
                stack.append(currDay)
        
        return waitDays 