class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        valid = []
        for num in nums:
            if nums.count(num) == 1:
                valid.append(num)
        
        return(valid)
    
print(Solution().singleNumber([-1,0]))