class Node:
    def __init__(self):
        self.childs = {} 
        self.isComplete = False

class WordDictionary:
    """
       Design a Trie to store strings
    """
    def __init__(self):
        self.root = Node() 

    def addWord(self, word: str) -> None:
        curr = self.root 
        for char in word:
            if char not in curr.childs:
                curr.childs[char] = Node() 
            curr = curr.childs[char]
        curr.isComplete = True

    def search(self, word: str) -> bool:
        """
            Traverse all the childrens if current char is a ".", otherwise we traverse current char children
        """
        def helper(word, root) -> bool:
            char = word[0]
            if len(word) == 1 and root.childs: 
                if char == ".":
                    return any([root.childs[node].isComplete for node in root.childs])
                
                elif char in root.childs:
                    return root.childs[char].isComplete 
            
            elif char in root.childs:
                return helper(word[1:], root.childs[char])
            
            elif char == ".": 
                for child in root.childs:
                    if helper(word[1:], root.childs[child]):
                        return True
                return False
            
            else:
                return False

        return helper(word, self.root)