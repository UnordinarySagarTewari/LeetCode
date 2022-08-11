class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        element=0
        for i in nums:
            if count == 0:
                element = i
            if element == i:
                count+=1
            else:
                count-=1
        return element
        
