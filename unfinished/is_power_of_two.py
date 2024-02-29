class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return(False)
        if n == 1: 
            return(True)
        else:
            return(self.isPowerOfTwo(n/2))

# num = Solution().isPowerOfTwo(0)
# print(num)