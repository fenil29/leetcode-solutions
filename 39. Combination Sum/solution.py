class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.combinationSumHelper(candidates, target, 0, 0, [], ans)
        return ans

    def combinationSumHelper(self, candidates, target, currSum, currElement, currElementList, ans):
        if (currSum > target):
            return
        currElementList.append(candidates[currElement])
        if (currSum == target):
            ans.append(currElementList[1:])
            return
        for i in range(currElement, len(candidates)):
            self.combinationSumHelper(
                candidates, target, currSum+candidates[i], i, currElementList.copy(), ans)
