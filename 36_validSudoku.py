def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. Loop thru each row and cell
            2. If cell not digit the skip to next cell
            3. ElIf match 2 conditions
            - cell match with any of the rest of the row elements
            - cell  match with any of rest of the col elements
            Then return false
        4. If every cell pass the conditions, then True
        """
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if not cell.isdigit():
                    continue

                otherRowItems = board[row][:col] + board[row][-1:col:-1]
                otherColItems = [board[r][col] for r in range(9) if r != row]

                #0-2, 3-5, 6-8 
                #0,1,2
                # row = 4, col 7
                rowBox = row // 3 * 3  # 3 
                colBox = col // 3 * 3  # 6

                # [3][6:6+3] [4][6:6+3] [5][6:6+3]
                boxItems = board[rowBox][colBox:colBox+3] + board[rowBox+1][colBox:colBox+3] + board[rowBox+2][colBox:colBox+3]

                if cell in otherRowItems or cell in otherColItems or boxItems.count(cell) > 1:
                    return False
        
        return True

def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. Define hashshet for each component
            a. rows
            b. cols
            c. boxes: a 3x3 box, each key will be a tuple(first_row, first_col)
        2. Loop thru each cell of the board, then check if it's already in the 3 hashset
        """
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)
        
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if not cell.isdigit():
                    continue

                box = (row // 3, col // 3)
                if cell in rows[row] or cell in cols[col] or cell in boxes[box]:
                    return False
                
                rows[row].append(cell)
                cols[col].append(cell)
                boxes[box].append(cell)

        
        return True