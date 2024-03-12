def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        3 cases:
        - c1 and c2 match: forward by 1 idx for both characters -> reuse the result of that pos and plus 1 
        - else: getting maximum of either c1 + 1, or c2 + 1 idx
        - final result: matrix[0][0]
        '''
        matrix = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]
        
        for row in range(len(matrix)-2, -1, -1):
            for col in range(len(matrix[0])-2, -1, -1):
                if text1[row] == text2[col]:
                    matrix[row][col] = matrix[row+1][col+1] + 1 
                else:
                    matrix[row][col] = max(matrix[row+1][col], matrix[row][col+1])
        
        return matrix[0][0]

