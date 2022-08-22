class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = 0
        minNum = 1
        maxNum = 1
        for i in nums:
            if i == 0:
                minNum = 1
                maxNum = 1
            else:
                product1 = i*minNum
                product2 = i*maxNum
                minNum = min(product1, product2, i)
                maxNum = max(product1, product2, i)
                ans = max(ans, maxNum)
        return ans
