class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        totalProduct = 1
        for i in range(len(nums)-1):
            totalProduct = totalProduct*nums[i]
            ans[i+1] = totalProduct
        totalProduct = 1
        for i in range(len(nums)-1, 0, -1):
            totalProduct = totalProduct*nums[i]
            ans[i-1] = ans[i-1]*totalProduct
        return ans
