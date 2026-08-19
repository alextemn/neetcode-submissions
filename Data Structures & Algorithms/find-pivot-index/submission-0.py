class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx = 0
        left, right = 0, sum(nums)
        
        while idx < len(nums):
            right -= nums[idx]
            if left == right:
                return idx
            left += nums[idx]
            idx += 1
        
        return -1    