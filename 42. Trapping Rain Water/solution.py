class Solution:
    def trap(self, height: List[int]) -> int:
        leftHighest=[None] * len(height)
        ans=0
        maxValue=0        
        for i in range(len(height)):
            maxValue=max(maxValue,height[i])
            leftHighest[i]=maxValue
        maxValue=0        
        for i in range(len(height)-1,-1,-1):
            maxValue=max(maxValue,height[i])
            leftHighest[i]=min(maxValue,leftHighest[i])
        for i,num in enumerate(leftHighest):
            water=num-height[i]
            if water<0:
                water=0
            ans=ans+water
        return ans