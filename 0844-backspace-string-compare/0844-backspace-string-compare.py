class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x = []
        for letter in s:
            if letter!='#':
                x.append(letter)
            elif x:
                x.pop()
        
        y = []
        for letter in t:
            if letter!='#':
                y.append(letter)
            elif y:
                y.pop()
        return ''.join(x)==''.join(y)
    
    