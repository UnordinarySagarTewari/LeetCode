class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans={}
        integer=""
        for i in word:
            if 'a'<=i<='z':
                if integer!="":
                    if int(integer) in ans:
                        ans[int(integer)]+=1
                    else:
                        ans[int(integer)]=1
                    integer=''
            else:
                integer+=i
        if integer!="":
            if int(integer) in ans:
                ans[int(integer)]+=1
            else:
                ans[int(integer)]=1
        return len(ans)
