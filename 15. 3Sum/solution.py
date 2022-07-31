class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        first=float("inf")
        for i in range(len(nums)-2):
            if(first==nums[i]):
                continue
            first=nums[i]            
            left=i+1
            right=len(nums)-1
            second=nums[left]
            third=nums[right]
            while left<right:
                while((first+second+third)<0 and left+1<right):
                    left+=1
                    second=nums[left]
                while((first+second+third)>0 and left+1<right):
                    right-=1 
                    third=nums[right]
                # print(i,left,right)
                if((first+second+third)==0):
                    ans.append([first,second,third])
                
                left=left+1
                while(left<len(nums) and nums[left]==second):
                    left=left+1
                if(left>=right):
                    break
                second=nums[left]
        return ans