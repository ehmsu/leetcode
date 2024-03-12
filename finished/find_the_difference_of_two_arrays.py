class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff1 = set([i for i in nums1 if i not in nums2])
        diff2 = set([i for i in nums2 if i not in nums1])

        return[diff1, diff2]