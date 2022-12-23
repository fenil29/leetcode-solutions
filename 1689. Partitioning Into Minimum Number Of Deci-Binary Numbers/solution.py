class Solution:
    def minPartitions(self, n: str) -> int:
        maxNum = int(n[0])
        for digit in n:
            digit = int(digit)
            if digit > maxNum:
                maxNum = digit
        return maxNum
