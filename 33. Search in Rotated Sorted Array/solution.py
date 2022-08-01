class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while(l <= r):
            numIndex = (r+l)//2
            print(numIndex, nums[numIndex], l, r)
            if nums[numIndex] == target:
                return numIndex
            elif nums[numIndex] < nums[r]:
                if nums[numIndex] > target:
                    r = numIndex-1
                else:
                    if nums[r] >= target:
                        l = numIndex+1
                    else:
                        r = numIndex-1
            else:
                if nums[numIndex] < target:
                    l = numIndex+1
                else:
                    if target < nums[l]:
                        l = numIndex+1
                    else:
                        r = numIndex-1

        return -1
