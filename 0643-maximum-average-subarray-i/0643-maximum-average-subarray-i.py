class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_ave = window_sum / k
        left = 0
        
        for right in range (k,len(nums)):
            window_sum -= nums[left]
            window_sum += nums[right]
            new_ave = window_sum/k
            max_ave = max(max_ave,new_ave)
            left += 1
        
        return max_ave


        
