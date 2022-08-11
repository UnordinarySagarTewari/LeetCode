class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        columns=len(matrix[0])
        
        def binarySearch(arr):
            l=0
            h=len(arr)-1
            while(l<=h):
                mid = (l+h)//2
                if arr[mid]==target:
                    return True
                elif target>arr[mid]:
                    l=mid+1
                else:
                    h=mid-1
            return False
                
                
            
        #Finding the row by using last column
        for row in range(rows):
            if target<=matrix[row][columns-1]:
                if binarySearch(matrix[row]):
                    return True
        return False
        
