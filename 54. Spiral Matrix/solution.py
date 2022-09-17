class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)
        ans = []
        if height == 1:
            return matrix[0]
        if width == 1:
            return [i[0] for i in matrix]
        i = 0
        while True:
            if(type(matrix[i][i]) == bool and matrix[i][i] == True):
                break
            j = i
            while j < width and type(matrix[i][j]) != bool:
                ans.append(matrix[i][j])
                matrix[i][j] = True
                j += 1
            j = i+1
            while j < height and type(matrix[j][width-1-i]) != bool:
                ans.append(matrix[j][width-1-i])
                matrix[j][width-1-i] = True
                j += 1
            j = i+1
            while j < width and type(matrix[height-1-i][width-1-j]) != bool:
                ans.append(matrix[height-1-i][width-1-j])
                matrix[height-1-i][width-1-j] = True
                j += 1
            j = i+1
            while j < height and type(matrix[height-1-j][i]) != bool:
                ans.append(matrix[height-1-j][i])
                matrix[height-1-j][i] = True
                j += 1
            i += 1
        return ans
