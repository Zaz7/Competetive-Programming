class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l,r = 0 ,len(height) - 1
        while l<r :
            area = (r-l)*min(height[r],height[l])
            maxarea = max(area,maxarea)
            if height[r]<height[l]:
                r-=1
            elif height[r]> height[l]:
                l+=1
            else :
                  r-=1
        return maxarea
                
        