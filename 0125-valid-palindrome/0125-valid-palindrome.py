class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        else:
            x = ""
            s= s.lower()
        
            for i in s:
                if i.islower() or i.isalnum() :
                    x+=i
            return x == x[::-1]