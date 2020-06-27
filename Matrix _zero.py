set matrix zero 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ZeroMatrix = False
        isCol = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                isCol = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,R):
            for j in range(1, C):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(C):
                matrix[0][i] = 0
        if isCol:
            for i in range(R):
                matrix[i][0] = 0
        '''m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        row_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                row_zero = True
        col_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                col_zero = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if col_zero:
            for j in range(n):
                matrix[0][j] = 0
        if row_zero:
            for i in range(m):
                matrix[i][0] = 0'''
                
