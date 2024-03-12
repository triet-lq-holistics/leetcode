def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
         - loop thru each cell
         - if cell value = 1, then we DFS. For each recursion, plus 1 to the area and call the next recursion for each direction if that direction hasn't been out of bound 
         - base case: the current value = 0 or it's out of boundary 
         - if the return value > cur_max, then replace cur_max 
        '''
        
        def dfs(row, col) -> int:
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            return 1 + dfs(row-1,col) + dfs(row+1,col) + dfs(row, col+1) + dfs(row, col-1)

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        

        return max_area 
