class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(s==t):
            return s
        if(t in s):
            return t
        start=end=0
        tCharCount,sCharCount={},{}
        sCharCount[s[start]]=1
        ansLen=len(s)+1
        ans=""

        for c in t:
            tCharCount[c]=tCharCount.get(c , 0) + 1
        while(end<len(s)): 
            ss=start
            ee=end
            while(end+1<len(s) and self.isValidString(sCharCount,tCharCount)==False):
                end=end+1
                char=s[end]
                sCharCount[char]=sCharCount.get(char , 0) + 1
   
            while(start<end and self.isValidString(sCharCount,tCharCount)!=False):
                char=s[start]
                if((end-start)+1<ansLen and self.isValidString(sCharCount,tCharCount)):
                    ansLen=(end-start)+1
                    ans=s[start:end+1]
                if(sCharCount.get(char,0)==1):
                    del sCharCount[char]
                else:
                    sCharCount[char]=sCharCount[char]-1   
                print(char,self.isValidString(sCharCount,tCharCount))
                start=start+1

            if(end>=len(s) or (ss==start and ee==end)):
                break
        return ans
            
    def isValidString(self,sCharCount,tCharCount):
        isValid=True
        for c in tCharCount:
            if(tCharCount[c]>sCharCount.get(c , 0)):
                isValid=False
        return isValid

