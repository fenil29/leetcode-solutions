class Solution:
    store = {}

    def climbStairs(self, n: int) -> int:
        if n in self.store:
            return self.store[n]
        else:
            ans = None
            if n == 0:
                ans = 1
            elif n < 0:
                ans = 0
            else:
                ans = self.climbStairs(n-1)+self.climbStairs(n-2)
            self.store[n] = ans
            return ans
