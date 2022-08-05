class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n=columnNumber
        ans=""
        while(n>0):
            c = chr(ord("A") + (n-1)%26)
            ans = c + ans
            n = (n-1)//26
        return ans
