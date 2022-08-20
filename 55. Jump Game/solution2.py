class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        reachableIndex = None
        i = len(nums)-1
        while i >= 0:
            step = 1
            while (i-step) >= 0:
                if nums[i-step] >= step:
                    reachableIndex = i-step
                    step = 1
                    break
                step = step+1
            i = i-step
        return reachableIndex == 0
