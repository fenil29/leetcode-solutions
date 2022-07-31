class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        queue=collections.deque()
        if k==1:
            return nums
       
        for num in nums[0:k]:
            while(len(queue)>0 and queue[-1]<num):
                queue.pop()
            queue.append(num)
        
        ans.append(queue[0])
        for i in range(k,len(nums)):
            numPrevious=nums[i-k]
            num=nums[i]
            if(numPrevious==queue[0]):
                queue.popleft()
            while(len(queue)>0 and queue[-1]<num):
                queue.pop()
            queue.append(num)
            ans.append(queue[0])
        return ans