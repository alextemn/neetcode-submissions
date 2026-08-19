class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        cur = height[len(height)-1]
        max_r = [cur] * len(height)

        for i in range(len(max_r)-1, 0, -1):
            cur = max(cur, height[i])
            max_r[i] = cur
        area = 0
        max_l = height[0]
        for i in range(1, len(height)):
            min_l_r = min(max_l,max_r[i])
        
            if min_l_r - height[i] > 0:
                area += min_l_r - height[i]
            
            max_l = max(max_l, height[i])
        return area