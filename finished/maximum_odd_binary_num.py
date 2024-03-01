class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = 0
        length = len(s)
        for i in list(s): 
            if i == "1":
                one_count += 1
        rem = length - one_count
        maximum_num = (one_count-1)*"1" + rem*"0"+"1"
        return(maximum_num)