class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        counter = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if i < j and nums[i]+nums[j]<target:
                        counter+=1
                    
                    
        return counter
        
        
        