class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # First pass: mark zeros in first row/col
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Second pass: use markers to set zeros (skip first row/col)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Handle first column if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Handle first row if needed
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0