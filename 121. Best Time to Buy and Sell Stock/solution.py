class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prvMin=float("inf")
        ans=0
        for i in range(len(prices)):
            if(prvMin<prices[i]):
                ans=max(ans,prices[i]-prvMin)
            prvMin=min(prvMin,prices[i])
        return ans
        