class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=len(nums1)-len(nums2)-1
        p2=len(nums2)-1
        i=len(nums1)-1
        while(p2>=0):
            if p1>=0 and nums1[p1]>nums2[p2]:
                nums1[i]=nums1[p1]
                i-=1
                p1-=1
            else:
                nums1[i]=nums2[p2]
                i-=1
                p2-=1
