class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        list_x_reversed = list(reversed(list_x))
        # print(list_x)
        # print(list_x_reversed)

        if list_x == list_x_reversed:
            return(True)
        else:
            return(False)
        

print(Solution().isPalindrome(121))