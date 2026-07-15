class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = sorted(nums1+nums2)
        if len(n)%2 == 0:
            mid = len(n)//2
            return (n[mid]+n[mid-1])/2
        else:
            return n[len(n)//2]