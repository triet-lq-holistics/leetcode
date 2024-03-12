def uniquePaths(self, m: int, n: int) -> int:
        '''
            base case: 1 
            recurrence relation: current_val = (row + 1) + (col-1) [top and left side]
        '''

        matrix = [[0] * n for _ in range(m)]
        matrix[0][0] = 1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col > 0:
                    matrix[row][col] += matrix[row][col-1]
                if row > 0: 
                    matrix[row][col] += matrix[row-1][col]
                    
        return matrix[-1][-1]
