class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix)
        for i in range(math.floor(width)//2):
            for j in range(i, width-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[width-1-j][i]
                matrix[width-1-j][i] = matrix[width-1-i][width-1-j]
                matrix[width-1-i][width-1-j] = matrix[j][width-1-i]
                matrix[j][width-1-i] = temp
