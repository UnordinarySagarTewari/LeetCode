class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i*2 in d:
                return True
            if i/2 in d:
                return True
            d[i]=1
        return False
