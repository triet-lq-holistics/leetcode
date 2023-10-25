def isPalindrome(s) -> bool:
    return s == s[::-1]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        - for each prefix, if the current prefix is palindrome, then recursive on its suffix to check if it's palindrome
        - base case: reach the leaf of the recursive tree (all the prefix in the recursion stack are palindrome)
        """
        ans = []
        def helper(ls, s):
            if not s:
                ans.append(ls[:])

            for idx,char in enumerate(s):
                prefix, suffix = s[:idx+1], s[idx+1:]
                if isPalindrome(prefix):
                    ls.append(prefix)
                    helper(ls, suffix)
                    ls.pop()

                
        helper([], s)
        return ans
            