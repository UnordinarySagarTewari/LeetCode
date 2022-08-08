class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n==1:
            return nums
        lastPeak=None
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                lastPeak=i
        if lastPeak==None:
            for i in range(n//2):
                nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
            return nums
        prevToLastPeak=lastPeak-1
        index=lastPeak
        for i in range(lastPeak,n):
            if nums[i]>nums[prevToLastPeak] and nums[i]<nums[lastPeak]:
                index=i
        nums[prevToLastPeak],nums[index] = nums[index],nums[prevToLastPeak]
        nums[lastPeak:]=sorted(nums[lastPeak:])
        
