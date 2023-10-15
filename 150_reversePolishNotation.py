def evalRPN(self, tokens: List[str]) -> int:
        """
        1. if operand is an integer, then push to stack
        2. Store the expr result as holding value 
        3. if operand is an operator, then 
            a. if there's no existing holding value. This operator will be executed for the top 2 value of the stack (assuming the arithmetic expr always valid)
            b. if there's already an existing holding value, then execute this operator to the holding value and the top value of the stack
        """
        operators = "+-*/"
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])
        
        for token in tokens:
            if token not in operators:
                stack.append(token)
            
            else:
                numRight = stack.pop()
                numLeft = stack.pop()
                
                result = eval(numLeft + token + numRight)
                result = int(result)  
                
                stack.append(str(result))
                
        return result