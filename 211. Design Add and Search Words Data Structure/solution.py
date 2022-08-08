class WordNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = WordNode()
            curr = curr.children[i]
        curr.isWordEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        currNodes = deque([curr])
        for char in word:
            for i in range(len(currNodes)):
                curr = currNodes.popleft()
                if char == ".":
                    for key in curr.children:
                        currNodes.append(curr.children[key])
                else:
                    if char in curr.children:
                        currNodes.append(curr.children[char])

        for char in currNodes:
            if char.isWordEnd == True:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
