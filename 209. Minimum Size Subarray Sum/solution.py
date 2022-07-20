class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        end=0
        sum=nums[0] if len(nums)>0 else 0
        ans=len(nums)+1
        while(end<len(nums)-1):
            if(start==end and nums[end]>=target):
                return 1
            end=end+1
            sum=sum+nums[end]
            while(start<end and (sum-nums[start])>=target):
                start=start+1
                sum=sum-nums[start-1]
            if(sum>=target):
                ans=min(ans,(end-start)+1)
        return 0 if ans==len(nums)+1 else ans