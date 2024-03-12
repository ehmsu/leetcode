class Solution:
    def customSortString(self, order: str, s: str) -> str:
        proper_s = ''
        for i in order: 
            while i in s: 
                proper_s += i
                s = s.replace(i,'', 1)
        return(proper_s+s)