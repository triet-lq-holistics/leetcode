def exist(self, board: List[List[str]], word: str) -> bool:
        """
        - look for the item
        - store a matrix of marked pos 
        - a loop to explore 4 directions
            - recursively move around to complete the word 
            - after each recursion, we return True if it's true
        -  after the loop of each recursion, return False (it means there's no correct path)
        """

        def helper(row, col, idx):
            nonlocal matrix
            if idx == len(word):
                return True
            
            # Move right
            if col + 1 < len(matrix[0]) and matrix[row][col+1] == 0 and board[row][col+1] == word[idx]: 
                matrix[row][col+1] = 1 
                right_bool = helper(row, col+1, idx+1)
                if right_bool:
                    return True
                
                matrix[row][col+1] = 0
            
            # Move down
            if row + 1 < len(matrix) and matrix[row+1][col] == 0 and board[row+1][col] == word[idx]: 
                matrix[row+1][col] = 1 
                down_bool = helper(row+1, col, idx+1)
                if down_bool:
                    return True
                matrix[row+1][col] = 0
            
            # Move left
            if col - 1 >= 0 and matrix[row][col-1] == 0 and board[row][col-1] == word[idx]: 
                matrix[row][col-1] = 1 
                left_bool = helper(row, col-1, idx+1)
                if left_bool:
                    return True
                matrix[row][col-1] = 0
            

            # Move down
            if row - 1 >= 0 and matrix[row-1][col] == 0 and board[row-1][col] == word[idx]: 
                matrix[row-1][col] = 1 
                down_bool = helper(row-1, col, idx+1)
                if down_bool:
                    return True
                matrix[row-1][col] = 0 
                
            return False
            
        # Initiate empty traversal matrix
        matrix = [[0]*len(board[0]) for _ in range(len(board))]
        
        # Look for starting point
        starts = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    starts.append((i,j))

        # Search word for each starting point
        for row,col in starts:
            matrix[row][col] = 1 
            res = helper(row, col, 1)
            if res:
                return True
            matrix[row][col] = 0

        return False