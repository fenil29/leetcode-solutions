class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=ans=-float("inf")
        for i in range(len(nums)):
            sum=max(nums[i],sum+nums[i])
            ans=max(ans,sum)
        return ans
        