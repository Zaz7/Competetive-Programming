class Solution(object):
    def fizzBuzz(self, n):
        
        
        """
        :type n: int
        :rtype: List[str]
        """
        ToT = [ ]
        for i in range (1,n+1):
            
            
            if i % 3 == 0 and i % 5 == 0:
                
                ToT.append("FizzBuzz")
            elif i % 3 == 0:
                ToT.append ("Fizz") 
            
            elif i % 5 == 0:
                ToT.append("Buzz")
             
            else:
                ToT.append(str(i))
        return ToT
