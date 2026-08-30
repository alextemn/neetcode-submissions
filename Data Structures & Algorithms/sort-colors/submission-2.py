class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r -= 1
        
        return nums