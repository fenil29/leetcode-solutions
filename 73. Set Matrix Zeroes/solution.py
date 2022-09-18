class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroCols = set()
        height = len(matrix)
        width = len(matrix[0])
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        for i in range(height):
            for j in zeroCols:
                matrix[i][j] = 0
        for i in range(width):
            for j in zeroRows:
                matrix[j][i] = 0
