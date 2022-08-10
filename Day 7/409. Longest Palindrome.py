class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=0
        
        odd=[d[i] for i in d if d[i]%2!=0]
        even=[d[i] for i in d if d[i]%2==0]
        if len(odd)>0:
            oddSum = sum(map(lambda x:x-1,odd))+1
        else:
            oddSum=0
        evenSum = sum(even)
        
        ans+=(oddSum+evenSum)
        return ans
