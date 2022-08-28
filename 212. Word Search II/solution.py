class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        width = len(board[0])
        height = len(board)
        ans = []
        trie = {}
        for word in words:
            self.addWord(trie, word)

        for i in range(height):
            for j in range(width):
                pass
                self.exploreNode(board, trie, width, height,
                                 i, j, "", trie, ans, set())
        return ans

    def addWord(self, trie, word):
        curr = trie
        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr["isEnd"] = True

    def removeWord(self, trie, word):
        path = []
        curr = trie
        for i in word:
            path.append(curr)
            curr = curr[i]
        for i in range(len(path)-1, 0, -1):
            temp = path[i][word[i]]
            if "isEnd" in temp:
                del temp["isEnd"]
            if len(temp) == 0:
                del path[i-1][word[i-1]][word[i]]

    def exploreNode(self, board, trie, width, height, i, j, currWord, currTrie, ans, seen):
        if i < 0 or j < 0 or j >= width or i >= height or (i, j) in seen:
            return
        seen.add((i, j))
        currChar = board[i][j]
        if currChar not in currTrie and "isEnd" in currTrie[currChar] and currTrie[currChar]["isEnd"]:
            ans.append(currWord+currChar)
            currTrie[currChar]["isEnd"] = False
            self.removeWord(trie, currWord+currChar)
        if currChar not in currTrie:
            return
        currTrie = currTrie[currChar]
        self.exploreNode(board, trie, width, height, i+1, j,
                         currWord+currChar, currTrie, ans, seen.copy())

        self.exploreNode(board, trie, width, height, i-1, j,
                         currWord+currChar, currTrie, ans, seen.copy())

        self.exploreNode(board, trie, width, height, i, j+1,
                         currWord+currChar, currTrie, ans, seen.copy())

        self.exploreNode(board, trie, width, height, i, j-1,
                         currWord+currChar, currTrie, ans, seen.copy())
