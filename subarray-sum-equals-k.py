class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x= 0 
        sum_= 0
        prefix_sum = {0 : 1}
        for n in nums:
            sum_+=n
            diff=sum_-k
            x+=prefix_sum.get(diff,0)
            prefix_sum[sum_] = 1 + prefix_sum.get(sum_,0)
        return x 
