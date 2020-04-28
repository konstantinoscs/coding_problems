# https://leetcode.com/problems/set-matrix-zeroes/
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    if not matrix:
        return
    row = set()
    col = set()
    rowl = len(matrix[0])
    for i, r in enumerate(matrix):
        for j, c in enumerate(r):
            if c == 0:
                row.add(i)
                col.add(j)
        
    for r in row:
        matrix[r] = [0]*rowl
    for j in col:
        for i in range(len(matrix)):
            matrix[i][j] = 0