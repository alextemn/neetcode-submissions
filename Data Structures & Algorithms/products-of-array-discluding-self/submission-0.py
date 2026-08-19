class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        res = []
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(prefix) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            s = prefix[i] * postfix[i]
            res.append(s)
        return res