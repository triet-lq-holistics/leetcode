

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