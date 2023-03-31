class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        left = 0
        right = k
        n = str(num)
        
        counter = 0
        start = 0
        end = k
        
        
        for iteration in range (0 , len(n)-k+1) :
            
            if int(n[left: right]) ==0:  
                left += 1
                right += 1
                #start += 1
                #end += 1
                    
            elif num % int(n[left: right]) == 0 :
                counter += 1
                left += 1
                right += 1
                #start += 1
                #end += 1
            
            else:
                left += 1
                right += 1
                #start += 1
                #end += 1
        
        return counter
    
            
                
                
                
            
        
        
        
       