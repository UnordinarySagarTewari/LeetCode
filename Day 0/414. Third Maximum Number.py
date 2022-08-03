class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            s.add(i)
        arr=sorted(list(s))
        if len(arr)<3:
            return arr[-1]
        else:
            return arr[-3]
