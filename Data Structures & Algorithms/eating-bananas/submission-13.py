class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = max(piles)
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            sum = 0
            for num in piles:
                sum += math.ceil(num / mid)
            if sum <= h:
                rate = min(rate, mid)
                right = mid - 1
            else:
                left = mid + 1
        return rate