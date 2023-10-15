

class Solution:
    """https://leetcode.com/problems/longest-substring-without-repeating-characters/description/"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        give 2 pointers started at index 0 and 1 
        Add them to a deque, 
        if the value of the right index is presented in the deque, 
            - Select the max between len of the deque vs the current max
            - pop the value until it no duplicated value, then push the current value into the deque
        if not, then add to the deque, add move right pointer forward by 1
        """

        subS = ''
        longestNum = 0

        for char in s:
            if char in subS:
                longestNum = max(longestNum, len(subS))
                while char in subS:
                    subS = subS[1:]    
            
            subS += char

        return max(longestNum, len(subS))
    

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window
        - Constrain metric: len() 
        - Numeric restriction of metric: no repeating chars in the substring
        - Most valid ans: longest substring without reapting

        Algo: 
            1. Loop thru s. Check if curr char is in the subStr
            2. If it is, then remove the leftmost char until there's none of curr char exist in subStr
            3. add curr char to substr 
            4. Update longest if curr subStr length is bigger than longest
        """

        subStr = ""
        longest = 0
        for char in s:
            while char in subStr: 
                subStr = subStr[1:]
            
            subStr += char
            longest = max(longest, len(subStr))

        return longest