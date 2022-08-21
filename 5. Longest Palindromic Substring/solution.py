class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        maxLengthIndex = (0, 0)
        for i in range(len(s)):
            left = right = i
            while (right+1) < len(s) and s[left] == s[right+1]:
                right = right+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left)+1 > maxLength:
                    maxLength = (right-left)+1
                    maxLengthIndex = (left, right)
                left = left-1
                right = right+1

        print(maxLength, maxLengthIndex)
        return s[maxLengthIndex[0]:maxLengthIndex[1]+1]
