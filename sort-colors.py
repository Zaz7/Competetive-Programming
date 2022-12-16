class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        current= 0
        r= len(nums) - 1
        while current <= r:
            if nums[current] == 0:
                nums[l],nums[current] = nums[current],nums[l]
                l+=1
                current+=1
            elif nums[current] ==2:
                nums[current],nums[r] = nums[r],nums[current]
                r-=1
            else:
                current+=1
