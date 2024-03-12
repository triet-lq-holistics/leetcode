def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] != 'O':
                return 
            
            board[row][col] = 'T'
            
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        
        # Transform un-surrounded cells to 'T'
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row in (0, ROWS-1) or col in (0, COLS-1)):
                    dfs(row, col)
        
        # Transform surrounded cells from 'O' -> 'X', and un-surrounded from 'T' -> 'O'
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
