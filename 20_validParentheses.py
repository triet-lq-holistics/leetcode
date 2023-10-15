def isValid(self, s: str) -> bool:
        """
        1. Declare a dict of open-closed parentheses 
        2. loop thru list
        3. if item is open parenthesis
            then push to stack
        4. else (it should be closed parenthesis), pop stack and check if it is the corresponding open parenthesis. return false if it's not 
        5. after loop complete, check if there's any item left in the ans array
        6. if it does, then return false, else return true
        """

        open_p = {
            "{": "}",
            "(": ")",
            "[": "]",
        }

        stack = []

        for p in s: 
            if p in open_p: 
                stack.append(p)
            elif len(stack) == 0:
                return False
            else:
                last_open_p = stack.pop()
                if open_p[last_open_p] != p:
                    return False
        
        if len(stack) > 0:
            return False