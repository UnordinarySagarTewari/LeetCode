class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=-10**9+1
        currSum=0
        if len(nums)==1:
            return nums[0]
        for i in nums:
            currSum+=i
            if currSum>maxSum:
                maxSum=currSum
            if currSum<0:
                currSum=0
        return maxSum
            
