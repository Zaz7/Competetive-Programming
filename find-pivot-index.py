otal= sum(nums)
        left_sum= 0 
        for i in range(len(nums)):
            right_sum = Total-nums[i]-left_sum
            if left_sum == right_sum:
                return i
            left_sum+=nums[i]
        return -1
            
