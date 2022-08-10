class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slowAgain = 0
        while True:
            slow = nums[slow]
            slowAgain = nums[slowAgain]
            if slow == slowAgain:
                return slow
        
