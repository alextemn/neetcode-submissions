class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, 0
        running_sum = 0

        while r < len(nums):
            if nums[r] >= target:
                return 1
            if running_sum < target:
                running_sum += nums[r]
                r += 1
            else:
                res = min(res, r-l)
                running_sum -= nums[l]
                l += 1
        
        while running_sum >= target:
            res = min(res, r-l)
            running_sum -= nums[l]
            l += 1

        if res == float('inf'):
            return 0
        return res