class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            neg = True
            x = -x
        else:
            neg = False 
        
        x_reversed = int(str(x)[::-1])

        if neg:
            x_reversed = -x_reversed
        
        if x_reversed < -2**31 or x_reversed > (2**31-1):
            return(0)

        else:
            return(x_reversed)
        
print(Solution().reverse(-2**32))