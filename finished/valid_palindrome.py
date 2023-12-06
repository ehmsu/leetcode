class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s.split())
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        if s[::-1] == s:
            return(True)
        else:
            return(False)
    
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))