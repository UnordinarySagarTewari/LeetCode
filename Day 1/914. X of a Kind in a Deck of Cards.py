class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d={}
        if len(deck)==1:
            return False
        if len(deck)==2:
            return deck[0]==deck[1]
        res = all(ele == deck[0] for ele in deck)
        if res:
            return True
        for i in deck:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=list(d.values())
        def gcd(x, y):
            while(y):
                x, y = y, x % y
            return x
        
        hcf = gcd(l[0],l[1])
        for i in range(2,len(l)):
            hcf = gcd(hcf,l[i])
        if hcf>1:
            return True
        else:
            return False
