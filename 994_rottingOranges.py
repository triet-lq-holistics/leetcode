from collections import deque
def orangesRotting(self, grid: list[list[int]]) -> int:
    '''
    BFS:
        - loop thru each cell, if this is a rotten orange, then BFS
        - For each level, add the adjacent cells to queue, and add 1 to local level
        - Repeating until there's no fresh orange
        - Replace global_min if local_level is smaller 
    '''
    ROWS, COLS = len(grid), len(grid[0])
    # Idenitfy rotten orange 
    queue = deque()
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 2:
                queue.append((row,col))

    # Start from each rotten orange, and rot any adjancent orange if it's fresh. Add that adjacent orange to the queue. Stop when it's empty or out of boundary.
    count = -1
    while queue: 
        for _ in range(len(queue)):
            row, col = queue.popleft()
            for x,y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + x, col + y
                
                if 0 <= new_row < ROWS and  0 <= new_col < COLS and grid[new_row][new_col] == 1 and (new_row,new_col) not in queue:
                    queue.append((new_row, new_col))
        
            grid[row][col] = 2
        
        count += 1

    # Loop thru the matrix again, if there's any fresh orange then return false 
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                return -1
    
    return max(count, 0)


test_cases = [
    [[2,1,1],[1,1,0],[0,1,1]], 
    [[2,1,1],[0,1,1],[1,0,1]],
    [[0,2]]
]

for test_case in test_cases:
    print(orangesRotting(test_case))