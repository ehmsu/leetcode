# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_combo_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        roman_numerals_dict = {"I": 1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0
        # print(len(s)*"0")
        
        # while s != len(s) * "0":
        for key in roman_combo_dict.keys():
            while key in s:
                # print(key)
                s = s.replace(key, "00", 1)
                number += roman_combo_dict[key]
        for key in roman_numerals_dict.keys():
            while key in s:
                s = s.replace(key, "0", 1)
                number += roman_numerals_dict[key]

        return(number)
    
print(Solution().romanToInt("MCMXCIV"))