class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        N = [0]*len(nums)
        l,r,x = 0,1,0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    N[x]+=1
            x+=1
        return N
            
        
        