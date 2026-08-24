class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f, s = 0, 0

        while True:
            f = nums[nums[f]]
            s = nums[s]

            if s == f:
                break
        
        s = 0

        while s != f:
            s = nums[s]
            f = nums[f]

        return s