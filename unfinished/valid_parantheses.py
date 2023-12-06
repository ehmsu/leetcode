class Solution:
    def isValid(self, s: str) -> bool:
        # # s = s.split("")
        # if "(" in s:
        #     try:
        #         idx = s.index(")")
        #         opening_idx = s.index("(")
        #         # print(opening_idx)
        #         # print(idx)
        #         # print(opening_idx-idx)
        #         if idx < opening_idx or abs(opening_idx-idx) > 1:
        #             raise ValueError
        #         else:
        #             return True
        #     except ValueError:
        #         return(False)
        # if "[" in s:
        #     try:
        #         idx = s.index("]")
        #         opening_idx = s.index("[")
        #         if idx < opening_idx or abs(opening_idx-idx) > 1:
        #             raise ValueError
        #         else:
        #             return True
        #     except ValueError:
        #         return(False)
        # if "{" in s:
        #     try:
        #         idx = s.index("}")
        #         opening_idx = s.index("{")
        #         if idx < opening_idx or abs(opening_idx-idx) > 1:
        #             raise ValueError
        #         else:
        #             return True
        #     except ValueError:
        #         return(False)

        
            
print(Solution().isValid("(){}}{"))