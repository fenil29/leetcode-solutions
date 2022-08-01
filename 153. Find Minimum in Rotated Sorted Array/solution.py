class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans=float("inf")
        while(l <= r):
            numIndex = (r+l)//2
            ans=min(ans,nums[numIndex])
            if nums[numIndex] < nums[r]:
                r=numIndex-1
            else:
                l=numIndex+1
        return ans