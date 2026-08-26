class Solution:        
    def findDuplicate(self, nums: List[int]) -> int:
        cur = 0
        while cur < len(nums):
            temp = nums[cur]

            if cur == temp-1:
                cur += 1
                continue
            else:
                if nums[cur] == nums[temp-1]:
                    return nums[cur]
                t = nums[temp-1]
                nums[temp-1] = nums[cur]
                nums[cur] = t