class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        y = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    y[i] += 1
        return y
