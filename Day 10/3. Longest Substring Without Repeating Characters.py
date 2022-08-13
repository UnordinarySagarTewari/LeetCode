class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        r=0
        length=0
        curr=0
        while(r<len(s)):
            if s[r] in d:
                l=max(d[s[r]]+1,l)
            d[s[r]]=r
            length = max(length,r-l+1)
            r+=1
        return length
                
                
        
