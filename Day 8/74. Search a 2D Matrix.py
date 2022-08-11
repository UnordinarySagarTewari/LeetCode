class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h=len(matrix)*len(matrix[0])-1
        l=0
        while(l<=h):
            mid = (l+h)//2
            r=mid//len(matrix[0])
            c=mid%len(matrix[0])
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                h=mid-1
            else:
                l=mid+1
        return False
        
