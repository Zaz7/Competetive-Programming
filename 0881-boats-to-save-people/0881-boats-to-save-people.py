class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_counter = 0
        l = 0
        r = len(people)-1 
        while l<=r :
            left_weight= limit- people[r]
            r-=1
            boat_counter+=1
            if l<=r and left_weight>= people[l]:
                l+=1
        return boat_counter
                    
                
        
                    
            
        
                
                