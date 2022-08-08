class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[]
        for i in range(1,numRows+1):
            icj=1
            row=[]
            for j in range(1,i+1):
                row.append(icj)
                icj = int(icj*(i-j)/(j))
            pascal.append(row)
        return pascal
