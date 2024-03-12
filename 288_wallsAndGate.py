def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2147483647
        # Looking for cell with 1 pos away from gate
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] in (-1, 0):
                    continue
                for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_row, new_col = row+x, col+y
                    if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS:
                        continue
                    if rooms[new_row][new_col] == 0 and (row,col) not in visited:
                        rooms[row][col] = 1
                        visited.add((row, col))

        # Expand in BFS 
        queue = deque(visited)
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_row, new_col = row+x, col+y
                    if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS:
                        continue

                    if rooms[new_row][new_col] == INF: 
                        rooms[new_row][new_col] = rooms[row][col] + 1 
                        queue.append((new_row, new_col))

