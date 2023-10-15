def characterReplacement(self, s: str, k: int) -> int:
        """
        Constraint metric: len 
        Numeric restriction: only k different letters exist in a repeating word
        Valid: longest 

        Algo: 
            1. store a dict with key is the char, and value is the occurences of that char in the subStr 
            2. Loop thru s 
            3. Add char to subStr
            4. Check if it's in substring
            5. If it's in the substring key-value and is the main char, then increase the key-value by one      
            6. Proceed while loop while total non-main char occurences exceed k 
                7. If it's in the substring, and it make the other key larger than the main char key value, then we update the current main char
                8. elif we need to remove leftmost char until it's valid

            9. update longest if the new subStr values sum is larger than longest
    ---
        In what case, the main char of the subStr should be modified to another one? 
            - When the value of 2 keys are equivalent, and if the curr char added making the other key has bigger value, then we switch main char to new key 

        - move right pointer in range of len(s)
        - update occurence of current right pointer
        - if total of non-max-occurences value > k, then move left pointer 

        """

        longest = 0
        occ = defaultdict(int)
        maxOcc = 0
        left = 0

        for right in range(len(s)): 
            occ[s[right]] += 1
            maxOcc = max(maxOcc, occ[s[right]])
            
            while (right - left + 1 - maxOcc) > k:
                occ[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest
