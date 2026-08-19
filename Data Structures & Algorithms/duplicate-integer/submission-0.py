class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mappings = {}
        for num in nums:
            if num in mappings:
                mappings[num] += 1
            else:
                mappings[num] = 1
        for obj in mappings:
            if mappings[obj] > 1:
                return True
        return False