class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        target_index=[]
        target_index_empty= []
        for i in range (len(sorted_nums)):
            if sorted_nums[i]==target:
                target_index.append(i)
        return target_index
            
