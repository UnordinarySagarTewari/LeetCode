class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l=list(flowerbed)
        if n==0:
            return True
        if len(l)==1:
            if l[0]==0:
                return n==1
        count=0
        if l[0]==0 and l[1]==0:
            count+=1
            l[0]=1
        if l[-1]==0 and l[-2]==0:
            count+=1
            l[-1]=1
        for i in range(1,len(flowerbed)-1):
            if l[i-1]==0 and l[i+1]==0 and l[i]==0:
                count+=1
                l[i]=1
        return count>=n
