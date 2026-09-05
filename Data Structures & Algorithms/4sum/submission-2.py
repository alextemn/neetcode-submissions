class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        prevI = None
        prevJ = None
        for i in range(len(nums) - 3):
            if prevI == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if prevI == nums[i] and prevJ == nums[j]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        left, right = nums[l], nums[r]
                        while l < len(nums) and nums[l] == left:
                            l += 1
                        while r >= 0 and nums[r] == right:
                            r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
                prevJ = nums[j]
            prevI = nums[i]
        
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        
        return res