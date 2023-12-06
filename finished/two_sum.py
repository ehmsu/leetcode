class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums2 = sorted(nums)
        # reverse_nums = nums[::-1]
        indices = []
        
        for num in nums2: 
            x = num 
            remainder = target - x 
            if remainder in nums2: 
                # y = nums2.index(remainder)
                indices.append(nums.index(x))
                idx = [i for i, x in enumerate(nums) if x == remainder]
                if len(idx) == 1:
                    indices.append(idx[0])
                else:
                    indices.append(idx[1])
                break
        
        return(indices)
    
test = Solution().twoSum([3, 3], 6)
print(test)