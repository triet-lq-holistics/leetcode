def letterCombinations(self, digits: str) -> List[str]:
        phoneBook = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        """
            for each digit in digits, extract all possible char and recursively call the function, on the prevStr + new char
        """
        if not digits:
            return []
        
        def helper(currStr, ans):
            idx = len(currStr)
            if idx == len(digits):
                ans.append(currStr) 
                return ans 

            for char in phoneBook[digits[idx]]:
                ans = helper(currStr + char, ans)
            
            return ans 
        
        return helper("", [])