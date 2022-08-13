class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left=j+1
                right=len(nums)-1
                new_target = target - nums[i]-nums[j]
                while(left<right):
                    if nums[left]+nums[right] == new_target:
                        quad = (nums[i],nums[j],nums[left],nums[right])
                        ans.append(quad)
                        while(left<right and nums[left]==quad[2]):
                            left+=1
                        while(left<right and nums[left]==quad[3]):
                            right-=1
                    elif nums[left]+nums[right] > new_target:
                        right-=1
                    else:
                        left+=1
        ans=list(map(list,set(ans)))
        return ans
                
                        
                        
