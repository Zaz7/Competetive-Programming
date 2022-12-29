class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack  = []
        i=0
        while(i<len(s)):
            if s[i]!= ')':
                stack.append(s[i])
            else: 
                stackpop= []
                while(stack[-1]!= '('):
                    stackpop.append(stack.pop())
                stack.pop()
                stack.extend(stackpop)
            i+=1
        return "".join(stack)
            
        