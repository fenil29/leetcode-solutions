class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        zeroIndexList = []
        for index, value in enumerate(nums):
            if value == 0:
                zeroIndexList.append(index)
        while len(zeroIndexList) > 0:
            i = 1
            zeroIndex = zeroIndexList.pop()
            while (zeroIndex-i) >= 0:
                if nums[zeroIndex-i] > i or (zeroIndex == len(nums)-1 and nums[zeroIndex-i] >= i):
                    break
                i += 1
            else:
                return False
        return True
