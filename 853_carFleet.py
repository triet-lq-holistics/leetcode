def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        - behind car cannot pass ahead car
        - behind car can catch up and drive at the same speed 
        - the ahead car will slow dow to the same speed as  the bedhind car
        
        - input is list of cars , output is a categories of those cars ( car fleets)
        - as long as 2 cars meet at some point, they will drive to the destination together

        Naive: 
        - Have a while loop, then an inner for loop represent each round 
        - For each round, we compare if there's any fleet that has the same position as another fleet 
        - Speed will be to the lower speed of the same fleet once one fleet catching up another one
        - We can update the position and speed accordingly and treat each item as one fleet -> the  arr length can be reduce by each round 

        Stack:
        - Idea: If the ahead fleet with the curr speed time-to-des less than the prev fleet, then it's ensured that theses 2 fleets will meet at a certain point and merge to one fleet(with the slower speed of the ahead fleet). WHich means that, we only care to the ahead fleet's speed only because that's the only fleet that still remain the speed
        - Algo:
            1. Pack pos and speed to one array of tuples and sort it by pos 
            2. Declare an empty stack and loop thru the arr in reverse order
            3. If the stack is not empty and the time-to-des of the curr item is less than the one in the stack, then we continue the loop
            4. Else (if the time-to-des is larger), which means that it will not catch the ahead fleet. Then we add to the stack time-to-des of the current fleet
            5. Once the loop complete, return len(stacK) which is our number of fleets
        """
        def get_eta(fleet: tuple) -> float:
            return (target - fleet[0]) / fleet[1]
            


        fleets = sorted(zip(position, speed))
        stack = [get_eta(fleets[-1])]

        for fleet in fleets[-2::-1]: 
            time = get_eta(fleet)
            if time > stack[-1]:
                stack.append(time)
        
        return len(stack)