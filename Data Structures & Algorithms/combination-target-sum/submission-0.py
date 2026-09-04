class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(cur, curSum, i):
            if curSum == target:
                res.append(cur.copy())
                return
            if curSum > target:
                return
            if i == len(nums):
                return
            
            cur.append(nums[i])
            backtrack(cur, curSum + nums[i], i)
            cur.pop()

            backtrack(cur, curSum, i + 1)

            return
        
        backtrack([], 0, 0)

        return res