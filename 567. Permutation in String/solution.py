class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowCharCount,s1CharCount={},{}
        for char in s1:
            s1CharCount[char] = s1CharCount.get(char,0)+1
        start=0
        end=len(s1)-1
        
        for char in s2[0:end+1]:
            windowCharCount[char]= windowCharCount.get(char,0)+1
            
        if(self.checkPermutation(windowCharCount,s1CharCount)):
            return True
            
        while(end+1<len(s2)):
            end+=1
            windowCharCount[s2[end]] = windowCharCount.get(s2[end],0)+1
            windowCharCount[s2[start]] -=1
            start=start+1 
            if(self.checkPermutation(windowCharCount,s1CharCount)):
                return True 
        return False
    
    def checkPermutation(self,windowCharCount,s1CharCount):
        for c in s1CharCount:
            if (c not in windowCharCount) or s1CharCount[c]!=windowCharCount[c]:
                return False
        return True
            