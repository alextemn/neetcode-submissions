class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        area = 0
        max_l, max_r = height[0], max(height[1:])
        for i in range(1, len(height)):
            min_l_r = min(max_l,max_r)
        
            if min_l_r - height[i] > 0:
                area += min_l_r - height[i]
            
            max_l = max(max_l, height[i])
            if i < len(height) - 1:
                max_r = max(height[i+1:])
        return area