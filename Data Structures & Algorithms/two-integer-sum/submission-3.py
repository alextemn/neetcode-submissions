class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        mappings = {}
        index = 0
        for num in nums:
            if num in mappings and num == target - num:
                solution.append(mappings[num])
                solution.append(index)
                solution.sort()
                return solution
            mappings[target - num] = index
            index += 1
        for num in nums:
            if num in mappings and num != target - num:
                solution.append(mappings[num])
        solution.sort()
        return solution 