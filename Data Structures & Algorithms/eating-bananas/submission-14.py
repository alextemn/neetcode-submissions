class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = float('inf')

        while l <= r:
            speed = 0
            mid = (l+r) // 2
            for p in piles:
                speed += math.ceil(p/mid)
            
            if speed > h:
                l = mid + 1
            else:
                r = mid - 1
                ans = min(ans, mid)
        
        return ans