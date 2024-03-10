class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        returned = []
        for i in nums1: 
            if i in nums2:
                returned.append(i)
                nums2.remove(i)
        return(returned)