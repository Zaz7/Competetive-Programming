class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)
        
        init_sum = sum(code[:k])
        final_sum = sum(code[k:n])
        left = 0
        right = k 
        lis = []
        m=n
        new_right = k
        
    
        if k > 0  :
            for i in range(n):
                
                
                
                
                if right < n:
                    init_sum -=code[left]
                    init_sum +=code[right]
                    right+=1
                    left+=1
                    lis.append(init_sum)
                
                else:
                    init_sum -=code[left]
                    init_sum +=code[(m)%n]
                    lis.append(init_sum)
                    left+=1
                    right+=1
                    m+=1
            return lis
        
        elif k==0:
            for i in range(n):
                lis.append(0)
            return lis
        
        else:
            lis.append(final_sum)
            
            for i in range(1,n):
                if new_right <= n: 
                    final_sum-=code[new_right]
                    final_sum+=code[left]
                    lis.append(final_sum)
                    left+=1
                    new_right+=1
            return lis
                    
                    
                    
                    
                