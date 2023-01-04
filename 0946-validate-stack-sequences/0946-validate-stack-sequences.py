class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j =0 
        for i in pushed:
            stack.append(i)
            while stack and j< len(popped) and popped[j]==stack[-1]:
                j+=1
                stack . pop()
        return stack == []
        
        