def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(low, high):
            for i in range(low, (low+high)//2):
                s[i], s[high+low-i-1] = s[high+low-i-1], s[i]
        
        reverse(0, len(s))
        pointer = 0 
        
        for i in range(len(s)+1):
            if i == len(s) or s[i] == " ":
                reverse(pointer, i)
                pointer = i + 1 
