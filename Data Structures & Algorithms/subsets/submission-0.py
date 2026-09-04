class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = set()
        def backtrack(cur, i):
            if i == len(nums):
                subs.add(tuple(cur))
                return
            
            backtrack(cur, i + 1)
            cur.append(nums[i])
            backtrack(cur, i + 1)
            cur.pop()

            return
        
        backtrack([], 0)
        
        subs = list(subs)
        for i in range(len(subs)):
            subs[i] = list(subs[i])
        
        return subs