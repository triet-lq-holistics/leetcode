class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        idx = 0 
        while idx < len(s):
            currentChar = s[idx]
            if (idx < len(s) - 1) and symbols[s[idx+1]] > symbols[currentChar]:
                subtraction = symbols[s[idx+1]] - symbols[currentChar]
                result += subtraction
                idx += 2
            
            else:
                result += symbols[currentChar]
                idx += 1
        
        return result