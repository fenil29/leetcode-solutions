class Solution:
    def trap(self, height: List[int]) -> int:
        leftHighest=[None] * len(height)
        rightHighest=[None] * len(height)
        ans=0
        maxValue=0        
        for i in range(len(height)):
            maxValue=max(maxValue,height[i])
            leftHighest[i]=maxValue
        maxValue=0        
        for i in range(len(height)-1,-1,-1):
            maxValue=max(maxValue,height[i])
            rightHighest[i]=maxValue
        for i,num in enumerate(height):
            totalCapacity=min(leftHighest[i],rightHighest[i])
            water=totalCapacity-num
            if water<0:
                water=0
            ans=ans+water
        return ans