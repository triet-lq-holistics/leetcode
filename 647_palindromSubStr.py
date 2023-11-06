def countSubstrings(self, s: str) -> int:
        '''
        1. go thru each index
        2. chekc for odd and even length of palindrome
        3. check for left and rightmost char for each exapnd subString of the curr index
        4. Continuously expand if the currSubStr is palindrome and still in range 
        '''

        count = 0 
        for idx in range(len(s)):
            count += 1 
            l, r = idx-1, idx+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1 
                r += 1 

            l, r = idx, idx+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1 
                r += 1 
        return count
