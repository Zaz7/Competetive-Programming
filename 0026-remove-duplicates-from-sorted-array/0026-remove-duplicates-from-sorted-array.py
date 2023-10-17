class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        x=[]
        x.append(nums[0])
        l=0
        
        for i in range(1,len(nums)):
            if nums[l] != nums[i]:
                x.append(nums[i])
            l+=1
            
        
        for i in range(len(x)):
            nums[i]=x[i]
        
        return len(x)
    
                
            
    

                
    