def longestPalindrome(self, s: str) -> str:
        '''
        Go from left to right. If currentStr is palindrome, then expand from left to right and check accordingly until the index is out of range 
        Check again for even palindrom

        1. Go thru each index of the array
        2. Check odd and even palindrome
        3. if curStr is palindrome then exapnd, else break 
        '''

        res = ''
        for idx in range(len(s)): 
            res1 = s[idx]
            l, r = idx-1, idx+1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res1 = s[l] + res1 + s[r]
                l -= 1
                r += 1 
                
            l, r = idx, idx+1
            res2 = ''
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res2 = s[l] + res2 + s[r]
                l -= 1
                r += 1 

            res = max([res, res1, res2], key=len)
        
        return res
