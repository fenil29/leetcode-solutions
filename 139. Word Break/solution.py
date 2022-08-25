class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakHelper(0, s, wordDict, {})

    def wordBreakHelper(self, i, s, wordDict, cache):
        if i == len(s):
            return True
        for word in wordDict:
            if s[i:].startswith(word):
                i2 = i+len(word)
                if i2 in cache:
                    if cache[i2]:
                        return True
                else:
                    ans = self.wordBreakHelper(i2, s, wordDict, cache)
                    cache[i2] = ans
                    if ans:
                        return True
        return False
