class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collection=set(nums)
        ans=0
        currentSeqLen=0
        while(len(collection)>0):
            currentSeqLen=1
            num=collection.pop()
            currNum=num+1
            while(currNum in collection):
                currentSeqLen=currentSeqLen+1
                collection.remove(currNum)
                currNum=currNum+1
            currNum=num-1
            while(currNum in collection):
                currentSeqLen=currentSeqLen+1
                collection.remove(currNum)
                currNum=currNum-1
            ans=max(ans, currentSeqLen)
        return ans        