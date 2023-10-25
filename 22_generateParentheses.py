def generateParenthesis(self, n: int) -> List[str]:
        """
        - keep track of current open and curr pairs
        - base case: curr open =0, and curr pairs = 3 
        - if curr open + curr pairs >= 3 => cannot open
        - if stack is empty => cannot closed
        """

        ans = []
        def helper(pairs: int, curr: str, stack: list):
            opens = len(stack)
            
            if opens == 0 and pairs == n:
                ans.append(curr)
                return
                
            if (opens + pairs) < n:
                helper(pairs, curr + "(", stack + "(")
            
            if len(stack) > 0:
                helper(pairs+1, curr + ")", stack[:-1])
        
        helper(0, "(", "(")
        return ans

def generateParenthesis(self, n: int) -> List[str]:
        """
        mimic-recursion implementation  as stack 
        """
        ans = []
        stack = [("(", "(", 0)]
        
        while stack:
            curr_str, curr_stack, done_pairs = stack.pop()
            if len(curr_str) == n*2:
                ans.append(curr_str)
            
            if len(curr_stack) > 0: 
                stack.append((curr_str + ")", curr_stack[:-1], done_pairs+1))
            
            if (done_pairs + len(curr_stack)) < n:
                stack.append((curr_str + "(", curr_stack + "(", done_pairs))
        return ans
