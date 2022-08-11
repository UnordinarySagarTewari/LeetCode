class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = None
        count1 = 0
        
        element2 = None
        count2 = 0
        for i in nums:
            if element1 == i:
                count1+=1
            elif element2 == i:
                count2+=1
            elif count1 == 0:
                element1 = i
                count1 = 1
            elif count2 == 0:
                element2 = i
                count2 = 1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for i in nums:
            if i == element1:
                count1+=1
            elif i == element2:
                count2+=1
        ans=[]
        if count1>len(nums)//3:
            ans.append(element1)
        if count2>len(nums)//3:
            ans.append(element2)
        return ans
        
            
        
