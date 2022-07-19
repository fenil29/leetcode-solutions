class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numOfCols = len(board[0])
        numfRows = len(board)
        columns = [set() for i in range(numOfCols)]
        rows = [set() for i in range(numfRows)]
        subBoard = [set() for i in range(9)]
        for i in range(numfRows):
            for j in range(numOfCols):
                num = board[i][j]
                if(num == "."):
                    continue
                if (num in columns[j]):
                    return False
                elif(num in rows[i]):
                    return False
                elif(num in subBoard[int(j/3)+(int(i/3)*3)]):
                    return False
                else:
                    columns[j].add(num)
                    rows[i].add(num)
                    rows[i].add(num)
                    subBoard[int(j/3)+(int(i/3)*3)].add(num)
        return True
