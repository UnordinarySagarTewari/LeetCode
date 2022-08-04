class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        a=arr
        if n<3:
            return False
        i=0
        up=0
        down=0
        while i<n-1:
            if a[i]>=a[i+1]:
                break
            up=1
            i+=1
        while i<n-1:
            if a[i]<=a[i+1]:
                break
            down=1
            i+=1
        return (i==n-1) and (up==1) and (down==1)
