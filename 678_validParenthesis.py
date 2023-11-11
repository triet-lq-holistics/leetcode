def checkValidString(self, s: str) -> bool:
        '''
        1. if "(" then add 1 
        2. if "*" then recursion on 3 sceneraio
        3. if ")" then minus 1 
        4. if result == -1, return False

        param: string idx, opens
        '''

        cache = {}

        def helper(idx, opens):
            if opens == -1:
                return False
            elif idx == len(s):
                return opens == 0
            
            elif (idx, opens) in cache:
                return cache[(idx, opens)]

            elif s[idx] == "(":
                cache[(idx, opens)] = helper(idx+1, opens + 1)
            
            elif s[idx] == ")":
                cache[(idx, opens)] = helper(idx+1, opens - 1)
            
            else:
                cache[(idx, opens)] = helper(idx+1, opens + 1) or helper(idx+1, opens) or helper(idx+1, opens - 1)
            
            return cache[(idx, opens)]
        

        return helper(0, 0)



                

def checkValidString(self, s: str) -> bool:
        '''
        greedy:
            1. max_opens and min_opens to store max and min possibility of open parentheses 
            2. eval each str's item
            3. +1 if (, -1 if ), +1 for max and -1 for min if * 
            4. return if min == 0
        '''
        max_opens, min_opens = 0, 0
        for item in s:
            if item == "(":
                max_opens += 1
                min_opens += 1
            elif item == ")":
                max_opens -= 1
                min_opens -= 1
            else:
                max_opens += 1
                min_opens -= 1
            
            if max_opens < 0:
                return False
            
            if min_opens < 0:
                min_opens = 0
        
        return min_opens == 0
