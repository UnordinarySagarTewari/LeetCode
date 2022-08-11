class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(n):
            ans=1
            while(n>1):
                ans*=n
                n-=1
            return ans
        
        down=m-1
        right=n-1
        
        return factorial(down+right)//(factorial(down)*factorial(right))
            
                
            
