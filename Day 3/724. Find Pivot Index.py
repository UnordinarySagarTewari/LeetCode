class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        curr=0
        for i in range(len(nums)):
            if curr==(s-nums[i])/2:
                return i
            else:
                curr+=nums[i]
        return -1
