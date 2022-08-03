class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count=0
        def incStrict(arr):
            for i in range(len(arr)-1):
                if arr[i]>=arr[i+1]:
                    return False
            return True
        for i in range(len(nums)):
            arr=nums[:i]+nums[i+1:]
            if incStrict(arr):
                return True
        return False
