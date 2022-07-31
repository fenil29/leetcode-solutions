class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            numIndex=math.floor((r+l)/2)
            num=nums[numIndex]
            if num<target:
                l=numIndex+1
            elif num>target:
                r=numIndex-1
            else:
                return numIndex
        return -1
            
        