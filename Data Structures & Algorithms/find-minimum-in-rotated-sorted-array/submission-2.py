class Solution:
    def findMin(self, nums: List[int]) -> int:
       left = 0
       right = len(nums) - 1
       mini = nums[left]
       if nums[left] < nums[right]:
        return nums[left]
       while left <= right:
        mid = left + (right - left) // 2
        print(nums[mid], mid) 
        mini = min(mini, nums[mid])
        print(mini)
        if nums[mid] > (nums[right]):
            left = mid + 1
        else:
            right = mid - 1
       return mini