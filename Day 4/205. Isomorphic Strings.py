class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x,y=len(s),len(t)
        if x!=y:
            return False
        hashcode=1
        d1={}
        S=[]
        for i in range(x):
            if s[i] in d1:
                S.append(d1[s[i]])
            else:
                d1[s[i]]=hashcode
                hashcode+=1
        hashcode=1
        d2={}
        T=[]
        for i in range(y):
            if t[i] in d2:
                T.append(d2[t[i]])
            else:
                d2[t[i]]=hashcode
                hashcode+=1
        return S==T
        
        
            
            
            
