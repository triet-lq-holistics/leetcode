def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        - s1 has a fixed length -> fixed window 
        naive:
        - move fixed window with a size of len(s1) thruout s2 
        - count occurences of each char in the window, and compare with s1 counter. 
        """

        s1Counter = Counter(s1)
        size = len(s1)
        s2Counter = Counter(s2[:size - 1 ])

        for i in range(size - 1, len(s2)):
            s2Counter[s2[i]] += 1
            
            if i > size - 1:
                s2Counter[s2[i-size]] -= 1

            if s2Counter == s1Counter:
                return True
        
        return False