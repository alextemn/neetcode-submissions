class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            curArea = max(curArea, h * (r-l))

            if h == heights[l]:
                l += 1
            else:
                r -= 1
        
        return curArea