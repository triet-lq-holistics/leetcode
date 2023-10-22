class Trie:
    """
     Use a dictionary as trie data structure, with a boolean flag to indicate whether current node is a complete word. 
     Each key-value in dictionary is another subtrie 
    """
    def __init__(self, isComplete: bool = False):
        self.trie = {} 
        self.isComplete = isComplete

    def insert(self, word: str) -> None:
        """
        if current char of word doesn't exist, then add to current leel of trie 
        """
        
        curr = self
        for char in word:
            if char not in curr.trie:
                curr.trie[char] = Trie()
            curr = curr.trie[char]
        
        curr.isComplete = True

    def search(self, word: str) -> bool:
        """
            loop thru each char, if char in key then continue to search thru that key as trie with the next char
            if loop complete then return true 
        """
        curr = self
        for char in word:
            if char not in curr.trie:
                return False
            curr = curr.trie[char]
        
        return True if curr.isComplete else False 


    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.trie:
                return False
            curr = curr.trie[char]
        
        return True