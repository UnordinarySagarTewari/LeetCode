class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #flip along y-axis i.e. horizontally
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
            
        
        
