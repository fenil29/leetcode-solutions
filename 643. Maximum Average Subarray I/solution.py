class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = 0
        currentAvg = 0
        sum = 0
        for i in range(k):
            sum = sum+nums[i]
        ans = sum/k
        for i in range(k, len(nums)):
            sum = sum+nums[i]-nums[i-k]
            currentAvg = sum/k
            ans = max(ans, currentAvg)
        return ans
