class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        mappings = {}
        j = 0
        out = []
        for i in range(len(nums), 0, -1):
            freq[i] = []
        for i in range(len(nums)):
            mappings[nums[i]] = 1 + mappings.get(nums[i], 0)
        for el in mappings:
            if mappings[el] in freq:
                freq[mappings[el]].append(el)
        for el in freq:
            if j >= k:
                return out
            if freq[el] != [] and len(freq[el]) >= k:
                return freq[el][:k]
            elif freq[el] != []:
                out += freq[el]
                j += len(freq[el])    
        return out