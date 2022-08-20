class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width = len(board[0])
        height = len(board)

        for i in range(height):
            for j in range(width):
                if self.existHelper(board, word, width, height, i, j, 0, set()):
                    return True
        return False

    def existHelper(self, board, word, width, height, i, j, index, seen):
        if (i, j) in seen or i < 0 or j < 0 or i >= height or j >= width or index >= len(word) or word[index] != board[i][j]:
            return False

        seen.add((i, j))
        if index+1 == len(word):
            return True
        else:
            return self.existHelper(board, word, width, height, i+1, j, index+1, seen.copy()) or \
                self.existHelper(board, word, width, height, i, j+1, index+1, seen.copy()) or \
                self.existHelper(board, word, width, height, i-1, j, index+1, seen.copy()) or \
                self.existHelper(board, word, width, height,
                                 i, j-1, index+1, seen.copy())
