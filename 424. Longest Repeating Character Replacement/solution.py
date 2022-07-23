class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=end=0
        charCount={}
        ans=0
        i=0
        while(end<len(s)):
            char=s[end]
            if (char in charCount):
                charCount[char]=charCount[char]+1
            else:
                charCount[char]=1
            while(self.isValidString(charCount,k,(end-start)+1)==False and start<=end):
                if charCount[s[start]]==1:
                    del charCount[s[start]]
                else:
                    charCount[s[start]]=charCount[s[start]]-1
                start=start+1
            ans=max(ans,(end-start)+1)
            end=end+1
        return ans
            
    def isValidString(self,charCount,k,length):
        isValid=False
        for char in charCount:
            if (length-charCount[char])<=k:
                isValid=True
        return isValid