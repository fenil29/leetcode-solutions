class Solution:
    def isPalindrome(self, s: str) -> bool:
        charStr=[e.lower() for e in s if e.isalnum()]
        return charStr==charStr[::-1]