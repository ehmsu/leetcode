# idea: 
# create arrays of 


class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0 
        arrays = (int) (n/7) * [list(range(1, 8))]
        rem_array = list(range(1, n%7+1))
        # print(rem_array)

        i = 0
        
        for i in range(0, (int)(n/7)):
            total += i*7+sum(arrays[i])
        # print(i)
        
        if (n<=7):
            total += sum(rem_array)
        else:
            total += (i+1)*len(rem_array) + sum(rem_array)
        return(total)

if __name__ == "__main__": 
    print(Solution().totalMoney(10))