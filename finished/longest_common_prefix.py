class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        counter = 1
        while counter <= len(strs[0]):
            first_letters = strs[0][:counter]
            if all(first_letters in word[:counter] for word in strs):
                # print("hallo")
                prefix = first_letters
            counter += 1
        return(prefix)
    
print(Solution().longestCommonPrefix(["c","acc","ccc"]))
