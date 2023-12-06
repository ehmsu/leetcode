class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = set(nums)
        nums.clear()
        nums += unique
        nums.sort()
        # print(nums)
        
        return(len(unique))

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))