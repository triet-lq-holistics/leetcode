from collections import Counter

def isAnagram(self, s: str, t: str) -> bool:
        """
        1. create a hashmap counter: char as key, and its occurences as value 
        2. everytime the key is hit, its value will be minused by 2 
        3. return true if all values are 0, else false
        """
        occ = Counter(s)
        for char in t: 
            val = occ.get(char)
            if val and val > 0:
                occ[char] -= 1 
            else:
                return False
        
        for val in occ.values():
            if val > 0:
                return False
        return True
