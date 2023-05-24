class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        l=len(str(x)) - 1
        x=str(x)
        while(l>r):
            if x[r] == x[l]:
                r+=1
                l-=1
                
            else:
                return False
        return True